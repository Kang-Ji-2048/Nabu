"""Check a portable reviewed data package without a database, GPU or base weights."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.label_review import evaluation_coverage, review_summary
from nabu.pipeline import timestamp

spec = importlib.util.spec_from_file_location('nabu_training_checks', Path(__file__).with_name('train-slm-mlx.py'))
training = importlib.util.module_from_spec(spec)
spec.loader.exec_module(training)


def check(dataset):
    dataset = Path(dataset)
    report = json.loads((dataset/'review-export.json').read_text())
    if not {'train.jsonl', 'validation.jsonl', 'preparation-manifest.json'} <= set(report.get('files', {})):
        raise ValueError('Reviewed package file inventory is incomplete')
    for name, expected in report['files'].items():
        if Path(name).name != name:
            raise ValueError('Package inventory must use local file names')
        if hashlib.sha256((dataset/name).read_bytes()).hexdigest() != expected:
            raise ValueError(f'Reviewed package file changed: {name}')
    train = training.read_partition(dataset/'train.jsonl', 'train')
    valid = training.read_partition(dataset/'validation.jsonl', 'validation')
    if report['counts'] != {'train': len(train), 'validation': len(valid)}:
        raise ValueError('Reviewed package counts differ from its data')
    if {row['id'] for row in train}.intersection(row['id'] for row in valid):
        raise ValueError('Training and validation identities overlap')
    if not any(row['target']['risks'] for row in train) or not any(not row['target']['risks'] for row in train):
        raise ValueError('Training must include supported and evidence-insufficient targets')
    def groups(rows):
        return {key for row in rows for key in
                [row['group'], row['epic'], *(item['id'] for item in [row['input']['plan']['root'], *row['input']['plan']['members']])]}
    if groups(train).intersection(groups(valid)):
        raise ValueError('Related plans cross train/validation')
    if max(timestamp(row['as_of'], mandatory=True) for row in train) >= min(timestamp(row['as_of'], mandatory=True) for row in valid):
        raise ValueError('Validation must follow training in time')
    manifest = training.validate_preparation(dataset/'preparation-manifest.json', train+valid)
    for name, key in (('grouping-proof.json','grouping_proof_sha256'), ('split-report.json','split_report_sha256')):
        if key in manifest and hashlib.sha256((dataset/name).read_bytes()).hexdigest() != manifest[key]:
            raise ValueError(f'Audited preparation proof changed: {name}')
    reviews = review_summary(train+valid)
    if any(report.get(key) != value for key, value in reviews.items()):
        raise ValueError('Package review provenance differs from sealed rows')
    return {'data_ready_for_experiment': True, 'training_started': False,
            'training_examples': len(train), 'validation_examples': len(valid),
            'training_positive_examples': sum(bool(row['target']['risks']) for row in train),
            **reviews, 'evaluation_coverage': evaluation_coverage(train, valid)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, default=Path(__file__).resolve().parents[1]/'data/training/xd-assistant-reviewed-v3')
    args = parser.parse_args()
    print(json.dumps(check(args.dataset), indent=2))


if __name__ == '__main__':
    main()
