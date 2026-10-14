"""Export explicit human or assistant decisions without rebuilding frozen inputs."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.risk.runner import validate_detection
from nabu.risk.contracts import Detection
from nabu.label_review import digest, evaluation_coverage, review_kind, review_summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidates', type=Path, required=True)
    parser.add_argument('--decisions', type=Path, required=True, help='JSONL: id, action=approve/revise/reject, reviewer; revised target required for revise')
    parser.add_argument('--preparation-manifest', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--reviewer-kind', choices=('human', 'assistant'), default='human',
                        help='Assistant review is recorded separately and never claims human approval')
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Choose a new approved dataset directory')
    manifest = json.loads(args.preparation_manifest.read_text())
    if manifest.get('version') != 'nabu-training-preparation-v1' or manifest.get('ready_for_training') is not True:
        raise ValueError('Preparation audit must pass before approved export')
    proof_files = {}
    for name, key in (('grouping-proof.json', 'grouping_proof_sha256'), ('split-report.json', 'split_report_sha256')):
        if key in manifest:
            path = args.preparation_manifest.parent/name
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != manifest[key]:
                raise ValueError(f'Preparation proof is missing or changed: {name}')
            proof_files[name] = path
    candidates = {}
    for line in args.candidates.read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row['id'] in candidates or row['split'] not in ('train', 'validation'):
            raise ValueError('Duplicate or non-development candidate')
        input_digest = hashlib.sha256(json.dumps(row['input'], sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        if manifest.get('inputs', {}).get(row['id']) != input_digest:
            raise ValueError('Candidate input differs from audited preparation')
        candidates[row['id']] = row
    selected, reviewed = [], set()
    for line in args.decisions.read_text().splitlines():
        if not line.strip():
            continue
        decision = json.loads(line)
        iid = decision['id']
        if iid in reviewed or iid not in candidates:
            raise ValueError('Duplicate or unknown review decision')
        reviewed.add(iid)
        reviewer = decision.get('reviewer')
        if not isinstance(reviewer, str) or not reviewer.strip():
            raise ValueError('Every decision requires a named reviewer')
        if decision.get('reviewer_kind', 'human') != args.reviewer_kind:
            raise ValueError('Decision reviewer kind differs from selected export policy')
        action = decision.get('action')
        if action == 'reject':
            continue
        if action not in ('approve', 'revise'):
            raise ValueError('Review must explicitly approve, revise or reject; pending decisions cannot export')
        row = candidates[iid]
        target = Detection.model_validate(decision['target'] if action == 'revise' else row['target']).model_dump()
        if validate_detection(target, row['input'])['rejected']:
            raise ValueError(f'Invalid approved citations: {iid}')
        exported = {**row, 'target': target,
                    'review_status': 'approved' if args.reviewer_kind == 'human' else 'assistant_reviewed',
                    'reviewer': reviewer.strip(), 'reviewer_kind': args.reviewer_kind,
                    'human_approved': args.reviewer_kind == 'human', 'review_action': action}
        if args.reviewer_kind == 'assistant':
            if (decision.get('input_sha256') != digest(row['input'])
                    or decision.get('candidate_target_sha256') != digest(row['target'])
                    or decision.get('target_sha256') != digest(target)):
                raise ValueError('Assistant decision must bind the candidate input and both target versions')
            exported['review'] = {key: decision.get(key) for key in ('reason', 'reviewed_at', 'input_sha256', 'target_sha256')}
            exported['review'].update(reviewer=reviewer.strip(), reviewer_kind='assistant', action=action)
            exported['candidate_labelling_questions'] = row.get('labelling_questions', [])
            exported['labelling_questions'] = []
            exported['review']['question_resolutions'] = decision.get('question_resolutions', [])
        else:
            exported['human_review_action'] = action
        review_kind(exported)
        selected.append(exported)
    if set(candidates) - reviewed:
        raise ValueError('Every candidate needs an explicit decision; review is incomplete')
    counts = {split: sum(r['split']==split for r in selected) for split in ('train', 'validation')}
    if not all(counts.values()):
        raise ValueError('Approved export requires nonempty train and validation partitions')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.'+args.output.name+'-', dir=args.output.parent))
    try:
        for split in ('train', 'validation'):
            (staging/f'{split}.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False)+'\n' for row in selected if row['split']==split))
        shutil.copyfile(args.preparation_manifest, staging/'preparation-manifest.json')
        for name, path in proof_files.items():
            shutil.copyfile(path, staging/name)
        report = {'counts': counts, 'pending_review': sorted(set(candidates)-reviewed),
                  'decision_sha256': hashlib.sha256(args.decisions.read_bytes()).hexdigest(),
                  'candidate_sha256': hashlib.sha256(args.candidates.read_bytes()).hexdigest(),
                  'preparation_manifest_sha256': hashlib.sha256(args.preparation_manifest.read_bytes()).hexdigest(),
                  'dataset_version': manifest.get('dataset_version'), 'training_started': False}
        report.update(review_summary(selected))
        report['files'] = {name: hashlib.sha256((staging/name).read_bytes()).hexdigest()
                           for name in ('train.jsonl', 'validation.jsonl', 'preparation-manifest.json', *proof_files)}
        report['evaluation_coverage'] = evaluation_coverage(
            [row for row in selected if row['split'] == 'train'],
            [row for row in selected if row['split'] == 'validation'])
        (staging/'review-export.json').write_text(json.dumps(report, indent=2)+'\n')
        if args.output.exists():
            raise ValueError('Output appeared concurrently')
        os.rename(staging, args.output)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
