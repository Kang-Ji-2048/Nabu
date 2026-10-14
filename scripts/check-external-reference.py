"""Verify frozen external AI references without opening source databases or calling a model."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.label_review import digest, review_kind
from nabu.pipeline import timestamp
from nabu.risk.runner import validate_detection

ROOT = Path(__file__).resolve().parents[1]


def read_rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def all_item_ids(rows):
    return {item['id'] for row in rows for item in
            [row['input']['plan']['root'], *row['input']['plan']['members'], *row['input']['prior_work']]}


def check(reference, roster, development):
    reference, roster, development = map(Path, (reference, roster, development))
    report = json.loads((reference/'reference-review.json').read_text())
    preparation = json.loads((reference/'preparation.json').read_text())
    if report.get('purpose') != 'external_reference_only_never_training' or preparation.get('purpose') != report['purpose']:
        raise ValueError('External reference purpose must remain evaluation only')
    if report.get('human_approved') is not False or report.get('independent_ground_truth') is not False:
        raise ValueError('AI references cannot claim independent human ground truth')
    required = {'reference-labels.jsonl', 'case-drafts.jsonl', 'preparation.json', 'semantic-audit.jsonl'}
    if not required <= set(report.get('files', {})):
        raise ValueError('External reference inventory is incomplete')
    for name, expected in report['files'].items():
        if Path(name).name != name or hashlib.sha256((reference/name).read_bytes()).hexdigest() != expected:
            raise ValueError(f'External reference file changed: {name}')
    if hashlib.sha256((roster/'case-roster.jsonl').read_bytes()).hexdigest() != preparation['roster_sha256']:
        raise ValueError('External roster changed after evidence preparation')
    locators = read_rows(roster/'case-roster.jsonl')
    drafts = read_rows(reference/'case-drafts.jsonl')
    refs = read_rows(reference/'reference-labels.jsonl')
    identities = [row['id'] for row in refs]
    if len(identities) != len(set(identities)) or set(identities) != {row['id'] for row in locators}:
        raise ValueError('External reference identities differ from the fixed roster')
    if len(refs) != report['sample_cases'] or len(refs) != preparation['sample_cases']:
        raise ValueError('External case counts differ from preparation')
    dev = read_rows(development/'train.jsonl')+read_rows(development/'validation.jsonl')
    if all_item_ids(refs).intersection(all_item_ids(dev)):
        raise ValueError('External evidence overlaps development identities')
    last_development = max(timestamp(row['as_of'], mandatory=True) for row in dev)
    frozen = {row['id']: row for row in drafts}
    fixed = {row['id']: row for row in locators}
    for row in refs:
        iid = row['id']
        if row['split'] != 'external_test' or review_kind(row) != 'assistant':
            raise ValueError('External references require the external_test split and sealed assistant review')
        if digest(row['input']) != preparation['inputs'][iid] or row['input'] != frozen[iid]['input']:
            raise ValueError('External input differs from the frozen historical draft')
        cutoff = timestamp(row['as_of'], mandatory=True)
        if cutoff < last_development or cutoff != timestamp(fixed[iid]['as_of'], mandatory=True) or cutoff != timestamp(row['input']['plan']['as_of'], mandatory=True):
            raise ValueError('External cutoff differs from the roster or predates development')
        if row['input']['plan']['root']['id'] != fixed[iid]['item_id']:
            raise ValueError('External root differs from the roster identity')
        if validate_detection(row['target'], row['input'])['rejected']:
            raise ValueError('External reference citations are invalid')
    positives = sum(bool(row['target']['risks']) for row in refs)
    if positives != report['positive_reference_cases']:
        raise ValueError('External positive counts differ from sealed references')
    return {'external_reference_ready': True, 'purpose': report['purpose'], 'sample_cases': len(refs),
            'positive_reference_cases': positives, 'human_approved': False,
            'independent_ground_truth': False, 'experimental': True, 'model_evaluation_started': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference', type=Path, default=ROOT/'data/external-test/mesos-ai-reference-v1')
    parser.add_argument('--roster', type=Path, default=ROOT/'data/external-test/mesos-roster-v1')
    parser.add_argument('--development', type=Path, default=ROOT/'data/training/xd-assistant-reviewed-v3')
    args = parser.parse_args()
    print(json.dumps(check(args.reference, args.roster, args.development), indent=2))


if __name__ == '__main__':
    main()
