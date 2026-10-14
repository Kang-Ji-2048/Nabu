"""Freeze the preselected external roster for blind reference labelling only."""
import argparse
from contextlib import closing
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.agents.evidence import freeze_evidence
from nabu.risk.runner import detector_input
from nabu.pipeline import timestamp
from nabu.label_review import digest


def prepare(database, roster_dir, output, development_labels, risk_types):
    database, roster_dir, output = Path(database), Path(roster_dir), Path(output)
    if output.exists():
        raise ValueError('Choose a new external-reference directory')
    protocol = json.loads((roster_dir/'protocol.json').read_text())
    roster_bytes = (roster_dir/'case-roster.jsonl').read_bytes()
    if hashlib.sha256(roster_bytes).hexdigest() != protocol['roster_sha256']:
        raise ValueError('Fixed external roster changed')
    roster = [json.loads(line) for line in roster_bytes.decode().splitlines() if line.strip()]
    if len(roster) != protocol['sample_cases'] or len({row['id'] for row in roster}) != len(roster):
        raise ValueError('External roster count or identities differ')
    development = [json.loads(line) for line in Path(development_labels).read_text().splitlines() if line.strip()]
    if not development or any(row['split'] not in {'train', 'validation'} for row in development):
        raise ValueError('Development inputs must contain train/validation only')
    development_ids = {item['id'] for row in development for item in
                       [row['input']['plan']['root'], *row['input']['plan']['members'], *row['input']['prior_work']]}
    upper_bound = max(timestamp(row['as_of'], mandatory=True) for row in development)
    with closing(sqlite3.connect(database.resolve().as_uri()+'?mode=ro', uri=True)) as db:
        if db.execute('SELECT source_key FROM project').fetchall() != [(protocol['project'],)]:
            raise ValueError('Use only the separately imported external project')
        identities = dict(db.execute('SELECT id, source_key FROM work_item'))
    if development_ids.intersection(identities):
        raise ValueError('External project overlaps development evidence')
    drafts = []
    for locator in roster:
        if locator['split'] != 'external_test' or identities.get(locator['item_id']) != locator['epic']:
            raise ValueError('External roster locator does not match imported identity')
        cutoff = timestamp(locator['as_of'], mandatory=True)
        if cutoff < upper_bound:
            raise ValueError('External cutoff predates development upper bound')
        frozen = freeze_evidence(database, locator['epic'], cutoff)
        payload = detector_input(frozen, risk_types, 12)
        drafts.append({**locator, 'group': locator['epic'], 'input': payload,
                       'evidence_fingerprint': frozen['evidence_fingerprint'], 'review_status': 'draft'})
    report = {'version': 'nabu-external-reference-preparation-v1', 'project': protocol['project'],
              'purpose': 'external_reference_only_never_training', 'sample_cases': len(drafts),
              'roster_sha256': protocol['roster_sha256'], 'development_trained_through': upper_bound,
              'development_labels_sha256': hashlib.sha256(Path(development_labels).read_bytes()).hexdigest(),
              'inputs': {row['id']: digest(row['input']) for row in drafts},
              'detector_predictions_used': False, 'outcomes_used_for_labels': False,
              'training_started': False, 'model_evaluation_started': False,
              'retrieval_policy': 'production detector_input lexical top 12; original fixed roster; one day after creation'}
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.'+output.name+'-', dir=output.parent))
    try:
        (staging/'case-drafts.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False)+'\n' for row in drafts))
        (staging/'preparation.json').write_text(json.dumps(report, indent=2)+'\n')
        if output.exists():
            raise ValueError('Output appeared concurrently')
        os.rename(staging, output)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--roster', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--development-labels', type=Path, required=True)
    parser.add_argument('--risk-types', nargs='+', required=True)
    args = parser.parse_args()
    result = prepare(args.database, args.roster, args.output, args.development_labels, args.risk_types)
    print(json.dumps({key: value for key, value in result.items() if key != 'inputs'}, indent=2))


if __name__ == '__main__':
    main()
