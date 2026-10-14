"""Create chronological 80/20 historical epic case specifications after ETL.

No labels or trained model claims are generated. Latest 20% remain held out.
"""
import argparse
from datetime import datetime, timedelta
import json
import math
from pathlib import Path
import sqlite3
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.agents.evidence import freeze_evidence
from nabu.risk.runner import detector_input


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--risk-types", nargs="+", required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("Choose a new output directory")
    with sqlite3.connect(args.database.resolve().as_uri() + '?mode=ro', uri=True) as db:
        tickets = db.execute("SELECT id, source_key, created_at FROM work_item ORDER BY created_at, source_key").fetchall()
        epics = db.execute("SELECT source_key, created_at FROM work_item WHERE type='epic' ORDER BY created_at, source_key").fetchall()
    rows = []
    for epic, created in epics:
        # Fixed, repeatable early review window. This is a historical partial plan,
        # not a claim about an unrecorded team planning meeting.
        cutoff = (datetime.fromisoformat(created.replace('Z', '+00:00')) + timedelta(days=1)).isoformat()
        frozen = freeze_evidence(args.database, epic, cutoff)
        rows.append({"id": epic, "epic": epic, "group": epic, "as_of": frozen['plan']['as_of'],
                     "input": detector_input(frozen, args.risk_types, 12),
                     "evidence_fingerprint": frozen['evidence_fingerprint'], "review_status": "draft"})
    if len(rows) < 5:
        raise ValueError("At least five epics are required")
    rows.sort(key=lambda row: (row['as_of'], row['id']))
    ticket_boundary = math.floor(len(tickets) * .8)
    ticket_validation = math.floor(ticket_boundary * .9)
    train_before = tickets[ticket_validation][2]
    eval_before = tickets[ticket_boundary][2]
    boundary = sum(row['as_of'] < eval_before for row in rows)
    validation = sum(row['as_of'] < train_before for row in rows)
    if validation == 0 or validation == boundary:
        raise ValueError("Not enough historical epics for nonempty training and validation")
    # Related plans crossing a boundary are excluded, never reassigned silently.
    memberships = {}
    for index, row in enumerate(rows):
        row['split'] = 'train' if index < validation else 'validation' if index < boundary else 'test'
        for item in [row['input']['plan']['root'], *row['input']['plan']['members']]:
            memberships.setdefault(item['id'], set()).add(row['split'])
    excluded = []
    retained = []
    for row in rows:
        conflicts = [item['id'] for item in [row['input']['plan']['root'], *row['input']['plan']['members']] if len(memberships[item['id']]) > 1]
        if conflicts:
            excluded.append({"id": row['id'], "reason": "shared plan tickets cross chronological partitions", "item_ids": conflicts})
        else:
            retained.append(row)
    args.output.mkdir(parents=True)
    for name, selected in [('development', tickets[:ticket_boundary]), ('train', tickets[:ticket_validation]),
                           ('validation', tickets[ticket_validation:ticket_boundary]), ('test', tickets[ticket_boundary:])]:
        (args.output / f'{name}-ticket-ids.jsonl').write_text(''.join(json.dumps({'id': row[0], 'source_key': row[1], 'created_at': row[2]}) + '\n' for row in selected))
    for split in ('train', 'validation', 'test'):
        selected = [row for row in retained if row['split'] == split]
        (args.output / f'{split}-drafts.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in selected))
    (args.output / 'case-specs.jsonl').write_text(''.join(json.dumps({k: row[k] for k in ('id','epic','group','as_of')}) + '\n' for row in retained))
    report = {"policy": "chronological_80_percent_development_20_percent_test", "unit": "ticket timeline boundaries applied to historical epic plans",
              "total_tickets": len(tickets), "development_tickets": ticket_boundary, "test_tickets": len(tickets)-ticket_boundary,
              "review_cutoff": "one day after epic creation", "total_epics": len(rows),
              "development_before_exclusions": boundary, "test_before_exclusions": len(rows)-boundary,
              "validation_within_development": boundary-validation,
              "train_before": train_before, "eval_before": eval_before,
              "counts": {split: sum(row['split']==split for row in retained) for split in ('train','validation','test')},
              "excluded": excluded, "labels_available": False,
              "limitations": ["Current epic type is used only to select dataset locators; historical model fields are reconstructed independently.", "A one-day review window may have little recoverable scope; inspect drafts before labelling.", "Grouping catches shared observed plan tickets, not semantic duplicates.", "Ratios are approximate when boundaries or exclusions affect counts."]}
    (args.output / 'split-report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
