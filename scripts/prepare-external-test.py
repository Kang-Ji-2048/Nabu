"""Create a frozen external-project test roster using identity/time metadata only."""
import argparse
from contextlib import closing
from datetime import datetime, timedelta
import hashlib
import json
from pathlib import Path
import random
import sqlite3
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.pipeline import timestamp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--project', required=True)
    parser.add_argument('--development-labels', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--sample-size', type=int, default=32)
    parser.add_argument('--seed', type=int, default=3407)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Choose a new external-test directory')
    if args.sample_size < 1:
        raise ValueError('Sample size must be positive')
    labels = [json.loads(line) for line in args.development_labels.read_text().splitlines() if line.strip()]
    if not labels or any(row['split'] not in ('train', 'validation') for row in labels):
        raise ValueError('Supply development labels only')
    seen_ids = {item['id'] for row in labels for item in [row['input']['plan']['root'], *row['input']['plan']['members'], *row['input']['prior_work']]}
    # Includes validation in case it informed hyperparameters/model selection.
    trained_through = max(timestamp(row['as_of'], mandatory=True) for row in labels)
    with closing(sqlite3.connect(args.database.resolve().as_uri() + '?mode=ro', uri=True)) as db:
        db.execute('BEGIN')
        projects = db.execute('SELECT id,source_key FROM project').fetchall()
        if len(projects) != 1 or projects[0][1] != args.project:
            raise ValueError('Use a separate database containing only the requested external project')
        project_id = projects[0][0]
        external_ids = {row[0] for row in db.execute('SELECT id FROM work_item WHERE project_id=?', (project_id,))}
        if external_ids & seen_ids:
            raise ValueError('External project overlaps supplied development evidence IDs')
        rows = db.execute("SELECT id,source_key,created_at FROM work_item WHERE project_id=? AND type='epic' ORDER BY created_at,source_key", (project_id,)).fetchall()
    eligible = []
    for iid, key, created in rows:
        cutoff = timestamp((datetime.fromisoformat(created.replace('Z', '+00:00')) + timedelta(days=1)).isoformat(), mandatory=True)
        if cutoff >= trained_through:
            eligible.append({'id': key, 'epic': key, 'item_id': iid, 'as_of': cutoff, 'split': 'external_test', 'reference_label_status': 'pending_independent_review'})
    if not eligible:
        raise ValueError('No external epics at or after the development label cutoff')
    sample = random.Random(args.seed).sample(eligible, min(args.sample_size, len(eligible)))
    sample.sort(key=lambda row: (row['as_of'], row['id']))
    args.output.mkdir(parents=True)
    roster = ''.join(json.dumps(row) + '\n' for row in sample)
    (args.output / 'case-roster.jsonl').write_text(roster)
    report = {'purpose': 'external_project_test_only', 'project': args.project, 'database': str(args.database.resolve()),
              'development_trained_through_upper_bound': trained_through,
              'development_label_sha256': hashlib.sha256(args.development_labels.read_bytes()).hexdigest(),
              'external_ticket_count': len(external_ids), 'external_epic_count': len(rows), 'eligible_epics': len(eligible),
              'sample_cases': len(sample), 'seed': args.seed,
              'roster_sha256': hashlib.sha256(roster.encode()).hexdigest(), 'overlap_with_development_ids': 0,
              'selection_policy': 'uniform sample of epic identity/time metadata, one day after creation, no selection by outcomes or predicted risks',
              'held_out_text_or_outcomes_used_for_selection': False, 'model_evaluation_started': False,
              'limitations': ['Selection uses snapshot epic type only as a locator.', 'Historical evidence recovery and independently reviewed test reference labels are still required.', 'This external test does not replace development validation or repair the XD membership audit.', 'Sample is not artificially balanced; absent positive reference risks would make risk recall undefined.']}
    (args.output / 'protocol.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
