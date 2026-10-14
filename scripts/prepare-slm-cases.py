"""Create chronological 80/20 historical epic case specifications after ETL.

No labels or trained model claims are generated. Latest 20% remain held out.
Use --development-only to reconstruct only training and validation examples.
"""
import argparse
from collections import defaultdict
from contextlib import closing
from datetime import datetime, timedelta
import json
import math
import os
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.agents.evidence import freeze_evidence
from nabu.pipeline import timestamp
from nabu.risk.runner import detector_input


def conservative_groups(db, epics):
    """Find potentially shared plan IDs using membership reference metadata only.

    All-time observations intentionally over-exclude plans compared with cutoff
    membership. No title, description, status, outcome or held-out plan is read.
    Jira IDs are extracted in SQL without retrieving raw Issue payloads.

    Return groups, unresolved parent references, identity ambiguities, and child
    IDs whose Epic Link cannot resolve to a supplied epic. Quarantined children
    are withheld independently of held-out partition membership.
    """
    items = db.execute("SELECT id, source_key, project_id FROM work_item").fetchall()
    by_key = defaultdict(set)
    for iid, key, project in items:
        by_key[(project, key)].add(iid)
    projects = {iid: project for iid, _, project in items}
    by_jira = defaultdict(set)
    for iid, jira in db.execute("""SELECT w.id,json_extract(r.payload,'$.Jira_ID')
            FROM raw_record r JOIN work_item w
            ON r.source=w.source AND r.source_id=substr(w.id,length(w.source)+2)
            WHERE r.table_name='Issue'"""):
        if jira is not None:
            by_jira[(projects[iid], str(jira))].add(iid)
    epic_ids = {row['item_id'] for row in epics}
    groups = {iid: {iid} for iid in epic_ids}
    unresolved = defaultdict(set)
    ambiguities = []
    quarantined_child_ids = set()

    def reference(project, label, jira):
        # Grouping must retain every possible identity, unlike historical
        # reconstruction, which withholds a conflicting field value.
        return (by_key.get((project, label), set()) |
                (by_jira.get((project, str(jira)), set()) if jira is not None else set()))

    for iid, field, before, after, from_id, to_id in db.execute("""
            SELECT item_id,field,from_value,to_value,from_id,to_id FROM event
            WHERE lower(field) IN ('epic child','epic link')"""):
        project = projects[iid]
        for side, label, jira in (('from', before, from_id), ('to', after, to_id)):
            if not label and jira is None:
                continue
            targets = reference(project, label, jira)
            if len(targets) > 1:
                ambiguities.append({'item_id': iid, 'field': field, 'side': side,
                                    'label': label, 'jira_id': jira,
                                    'candidate_item_ids': sorted(targets)})
            if field.casefold() == 'epic child' and iid in epic_ids:
                if targets:
                    groups[iid].update(targets)
                else:
                    unresolved[iid].add((label, jira))
            elif field.casefold() == 'epic link':
                parents = targets & epic_ids
                if not parents:
                    # Its parent partition is unknown. Withhold this known child
                    # from every development input, including prior evidence.
                    quarantined_child_ids.add(iid)
                for parent in parents:
                    groups[parent].add(iid)
    ambiguities.sort(key=lambda row: json.dumps(row, sort_keys=True))
    return groups, unresolved, ambiguities, quarantined_child_ids


def prepare_cases(database, output, risk_types, *, development_only=False):
    database, output = Path(database), Path(output)
    if output.exists():
        raise ValueError("Choose a new output directory")
    with closing(sqlite3.connect(database.resolve().as_uri() + '?mode=ro', uri=True)) as db:
        db.execute('BEGIN')
        tickets = db.execute("SELECT id, source_key, created_at FROM work_item ORDER BY created_at, source_key").fetchall()
        epics = db.execute("SELECT id, source_key, created_at FROM work_item WHERE type='epic' ORDER BY created_at, source_key").fetchall()
        if len(epics) < 5:
            raise ValueError("At least five epics are required")
        ticket_boundary = math.floor(len(tickets) * .8)
        ticket_validation = math.floor(ticket_boundary * .9)
        train_before = tickets[ticket_validation][2]
        eval_before = tickets[ticket_boundary][2]
        locators = []
        for iid, epic, created in epics:
            # Fixed review window; not an unrecorded planning meeting.
            cutoff = timestamp((datetime.fromisoformat(created.replace('Z', '+00:00')) + timedelta(days=1)).isoformat(), mandatory=True)
            split = 'train' if cutoff < train_before else 'validation' if cutoff < eval_before else 'test'
            locators.append({'item_id': iid, 'id': epic, 'epic': epic, 'group': epic,
                             'as_of': cutoff, 'split': split})
        metadata_groups, unresolved, ambiguities, quarantined_child_ids = conservative_groups(db, locators) if development_only else ({}, {}, [], set())
    locators.sort(key=lambda row: (row['as_of'], row['id']))
    initial_counts = {split: sum(row['split'] == split for row in locators) for split in ('train', 'validation', 'test')}
    if not initial_counts['train'] or not initial_counts['validation']:
        raise ValueError("Not enough historical epics for nonempty training and validation")
    excluded = []
    metadata_partitions = defaultdict(set)
    held_out_evidence_ids = set()
    excluded_evidence_ids = set()
    if development_only:
        unsafe = sorted(row['id'] for row in locators if row['split'] == 'test' and unresolved.get(row['item_id']))
        if unsafe:
            raise ValueError(f'Unresolved held-out Epic Child references for {", ".join(unsafe)}; no files were published')
        for row in locators:
            for iid in metadata_groups[row['item_id']]:
                metadata_partitions[iid].add(row['split'])
            if row['split'] == 'test':
                held_out_evidence_ids.update(metadata_groups[row['item_id']])
        excluded_evidence_ids = held_out_evidence_ids | quarantined_child_ids
    rows = []
    for locator in locators:
        if development_only and locator['split'] == 'test':
            continue
        if development_only:
            conflicts = sorted(iid for iid in metadata_groups[locator['item_id']] if len(metadata_partitions[iid]) > 1)
            quarantined = sorted(metadata_groups[locator['item_id']] & quarantined_child_ids)
            if conflicts or quarantined or unresolved.get(locator['item_id']):
                excluded.append({'id': locator['id'], 'split': locator['split'],
                                 'reason': ('conservative all-time membership metadata overlaps chronological partitions' if conflicts else
                                            'plan group contains a child with an unresolved Epic Link' if quarantined else
                                            'unresolved membership references prevent complete group checks'),
                                 'item_ids': conflicts,
                                 'quarantined_item_ids': quarantined,
                                 'unresolved_reference_count': len(unresolved.get(locator['item_id'], []))})
                continue
        if development_only:
            frozen = freeze_evidence(database, locator['epic'], locator['as_of'], exclude_evidence_ids=excluded_evidence_ids)
        else:
            frozen = freeze_evidence(database, locator['epic'], locator['as_of'])
        row = {key: value for key, value in locator.items() if key != 'item_id'}
        row.update({'as_of': frozen['plan']['as_of'], 'input': detector_input(frozen, risk_types, 12),
                    'evidence_fingerprint': frozen['evidence_fingerprint'], 'review_status': 'draft'})
        rows.append(row)
    # Also validate actual supplied membership, including the all-splits mode.
    memberships = defaultdict(set)
    for row in rows:
        for item in [row['input']['plan']['root'], *row['input']['plan']['members']]:
            memberships[item['id']].add(row['split'])
    retained = []
    for row in rows:
        conflicts = sorted(item['id'] for item in [row['input']['plan']['root'], *row['input']['plan']['members']] if len(memberships[item['id']]) > 1)
        if conflicts:
            excluded.append({'id': row['id'], 'split': row['split'], 'reason': 'shared plan tickets cross chronological partitions', 'item_ids': conflicts})
        else:
            retained.append(row)
    splits = ('train', 'validation') if development_only else ('train', 'validation', 'test')
    counts = {split: sum(row['split'] == split for row in retained) for split in splits}
    if not counts['train'] or not counts['validation']:
        raise ValueError("Group exclusions leave an empty training or validation split; no files were published")
    report = {'policy': 'chronological_80_percent_development_20_percent_test',
              'unit': 'ticket timeline boundaries applied to historical epic plans',
              'development_only': development_only, 'total_tickets': len(tickets),
              'development_tickets': ticket_boundary, 'test_tickets': len(tickets) - ticket_boundary,
              'review_cutoff': 'one day after epic creation', 'total_epics': len(locators),
              'development_before_exclusions': initial_counts['train'] + initial_counts['validation'],
              'test_before_exclusions': initial_counts['test'],
              'validation_within_development': initial_counts['validation'],
              'train_before': train_before, 'eval_before': eval_before,
              'counts': counts, 'excluded': excluded, 'labels_available': False,
              'held_out_reconstructed': not development_only,
              'held_out_evidence_ids_excluded': len(held_out_evidence_ids),
              'quarantined_child_count': len(quarantined_child_ids),
              'quarantined_child_ids': sorted(quarantined_child_ids),
              'evidence_ids_excluded': len(excluded_evidence_ids),
              'membership_ambiguities': ambiguities,
              'group_check': 'conservative_all_time_membership_reference_metadata' if development_only else 'supplied_historical_plan_membership',
              'limitations': ['Current epic type is used only to select dataset locators; historical model fields are reconstructed independently.',
                              'A one-day review window may have little recoverable scope; inspect drafts before labelling.',
                              'Grouping catches shared observed plan tickets, not semantic duplicates.',
                              'Ratios are approximate when boundaries or exclusions affect counts.']}
    if development_only:
        report['limitations'].append('Held-out cutoff plans are not reconstructed or emitted. Their roots and all-time observed members are withheld from development prior evidence, including prior scope reconstruction containing those references. HistoricalReader still loads underlying source records internally for historical reconstruction. Cross-partition exclusion uses membership reference metadata and can conservatively exclude memberships absent at a review cutoff.')
        report['limitations'].append('Conflicting membership identities contribute every resolvable candidate to group checks. Unresolved held-out parent references stop preparation before reconstruction. Children with unresolved Epic Links are quarantined from development plans and evidence without assigning them a held-out partition.')
    # Publish the complete directory only after successful reconstruction/checks.
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f'.{output.name}-', dir=output.parent))
    try:
        ticket_sets = [('development', tickets[:ticket_boundary]), ('train', tickets[:ticket_validation]),
                       ('validation', tickets[ticket_validation:ticket_boundary])]
        if not development_only:
            ticket_sets.append(('test', tickets[ticket_boundary:]))
        for name, selected in ticket_sets:
            (staging / f'{name}-ticket-ids.jsonl').write_text(''.join(json.dumps({'id': row[0], 'source_key': row[1], 'created_at': row[2]}) + '\n' for row in selected), encoding='utf-8')
        for split in splits:
            selected = [row for row in retained if row['split'] == split]
            (staging / f'{split}-drafts.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in selected), encoding='utf-8')
        (staging / 'case-specs.jsonl').write_text(''.join(json.dumps({k: row[k] for k in ('id', 'epic', 'group', 'as_of')}) + '\n' for row in retained), encoding='utf-8')
        (staging / 'split-report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        # Never replace a directory created concurrently by another run.
        if output.exists():
            raise ValueError('Output directory appeared during preparation; no files were replaced')
        os.rename(staging, output)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--risk-types', nargs='+', required=True)
    parser.add_argument('--development-only', action='store_true', help='Reconstruct and emit only train/validation; group checks use membership reference metadata without reconstructing held-out plans')
    args = parser.parse_args()
    print(json.dumps(prepare_cases(args.database, args.output, args.risk_types, development_only=args.development_only), indent=2))


if __name__ == '__main__':
    main()
