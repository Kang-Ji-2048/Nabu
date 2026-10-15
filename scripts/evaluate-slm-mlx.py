"""Compare a frozen MLX base and trained adapter on sealed external references.

References are experimental AI assessments, never independent ground truth.
No training, prompt tuning, truncation, export, or model serving is performed.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nabu.risk.contracts import Detection
from nabu.risk.runner import validate_detection
from nabu.slm import messages


def save(path, value):
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def sha(path):
    with path.open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()


def assess(text, finish_reason, payload):
    result = {'schema_valid': False, 'human_assessment': None}
    try:
        if finish_reason != 'stop':
            raise ValueError('Generation did not reach EOS; incomplete output is not scored as no risk')
        submission = Detection.model_validate_json(text).model_dump()
        checked = validate_detection(submission, payload)
        result.update(schema_valid=True, submission=submission,
                      proposed_findings=len(submission['risks']),
                      valid_findings=len(checked['risks']),
                      validated_risks=checked['risks'], citation_errors=checked['rejected'])
    except ValueError as exc:
        result['error'] = str(exc)
    return result


def summarize(results, refs):
    by_id = {r['id']: r for r in refs}
    valid = [r for r in results if r['schema_valid']]
    proposed = sum(r['proposed_findings'] for r in valid)
    positives = [r for r in valid if by_id[r['id']]['target']['risks']]
    negatives = [r for r in valid if not by_id[r['id']]['target']['risks']]
    return {'completed_cases': len(results), 'schema_valid_cases': len(valid),
            'proposed_findings': proposed,
            'citation_valid_finding_fraction': sum(r['valid_findings'] for r in valid)/proposed if proposed else None,
            'ai_positive_reference_cases': sum(bool(r['target']['risks']) for r in refs),
            'scorable_ai_positive_cases': len(positives),
            'ai_positive_cases_with_any_valid_finding': sum(r['valid_findings'] > 0 for r in positives),
            'scorable_ai_negative_cases': len(negatives),
            'ai_negative_cases_with_any_valid_finding': sum(r['valid_findings'] > 0 for r in negatives),
            'human_usefulness_false_alarm_assessment': None}


def worker(args, rows):
    import mlx.core as mx
    from mlx_lm import load, stream_generate
    from mlx_lm.sample_utils import make_sampler
    mx.random.seed(3407)
    adapter = str(args.run/'adapters') if args.arm == 'adapter' else None
    model, tokenizer = load(str(args.model), adapter_path=adapter)
    # Preflight every prompt before the first inference. Targets never enter prompts.
    prompts = [tokenizer.apply_chat_template(messages(r['input']), tokenize=True,
               add_generation_prompt=True, enable_thinking=False) for r in rows]
    if any(len(p) + args.max_tokens > args.context for p in prompts):
        raise ValueError('Context budget exceeded; no evidence was truncated')
    report = {'arm': args.arm, 'trained': args.arm == 'adapter', 'status': 'running',
              'results': [], 'metrics': {}, 'reference_is_independent_ground_truth': False}
    destination = args.output/f'{args.arm}.json'
    save(destination, report)
    for index, (row, prompt) in enumerate(zip(rows, prompts), 1):
        started = time.monotonic()
        chunks, last = [], None
        for chunk in stream_generate(model, tokenizer, prompt, max_tokens=args.max_tokens,
                                     sampler=make_sampler(temp=0), prefill_step_size=512):
            chunks.append(chunk.text)
            last = chunk
        text = ''.join(chunks)
        entry = {'id': row['id'], 'prompt_tokens': len(prompt), 'raw_output': text,
                 'finish_reason': last.finish_reason if last else None,
                 'generation_tokens': last.generation_tokens if last else 0,
                 'elapsed_seconds': round(time.monotonic()-started, 3),
                 **assess(text, last.finish_reason if last else None, row['input'])}
        report['results'].append(entry)
        report['metrics'] = summarize(report['results'], rows)
        save(destination, report)
        print(f"{args.arm} {index}/{len(rows)} {row['id']} schema={entry['schema_valid']} "
              f"valid_findings={entry.get('valid_findings', 'unscorable')} seconds={entry['elapsed_seconds']}", flush=True)
        del last, chunks
        mx.clear_cache()
    report['status'] = 'completed'
    save(destination, report)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', type=Path, default=ROOT/'data/models/qwen3-8b-mlx-4bit')
    parser.add_argument('--run', type=Path, default=ROOT/'data/training/run-epoch1')
    parser.add_argument('--reference', type=Path, default=ROOT/'data/external-test/mesos-ai-reference-v1')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--context', type=int, default=16384)
    parser.add_argument('--max-tokens', type=int, default=2048)
    parser.add_argument('--arm', choices=['compare', 'baseline', 'adapter'], default='compare')
    args = parser.parse_args()
    rows = [json.loads(line) for line in (args.reference/'reference-labels.jsonl').read_text().splitlines() if line.strip()]
    if args.arm != 'compare':
        worker(args, rows)
        return
    spec = importlib.util.spec_from_file_location('external_check', ROOT/'scripts/check-external-reference.py')
    check = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(check)
    audit = check.check(args.reference, ROOT/'data/external-test/mesos-roster-v1', ROOT/'data/training/xd-assistant-reviewed-v3')
    trained = json.loads((args.run/'training-run.json').read_text())
    base = json.loads((args.model/'nabu-base.json').read_text())
    if trained['status'] not in {'experimental_adapter_trained', 'trained'} or any(
            base.get(k) != trained['base_provenance'][k] for k in ('checkpoint', 'revision', 'bits')):
        raise ValueError('Finished training and matching pinned base provenance required')
    if args.context < 16384 or args.max_tokens != 2048:
        raise ValueError('Frozen comparison requires context >=16384 and output budget 2048')
    args.output.mkdir(parents=True, exist_ok=False)
    manifest = {'status': 'running', 'started_at': datetime.now(timezone.utc).isoformat(),
                'arms': ['baseline', 'adapter'], 'reference_audit': audit,
                'base_provenance': base, 'reference_sha256': sha(args.reference/'reference-labels.jsonl'),
                'adapter_sha256': sha(args.run/'adapters/adapters.safetensors'),
                'training_run_sha256': sha(args.run/'training-run.json'),
                'script_sha256': sha(Path(__file__)), 'context_budget': args.context,
                'max_output_tokens': args.max_tokens, 'temperature': 0, 'enable_thinking': False,
                'limitations': ['AI reference agreement is not human-verified precision or recall.',
                                'Citation checks validate exact evidence references, not semantic support.',
                                'Raw model JSON is scored without repair or grammar constraints.',
                                'No export or deployment quantization comparison has been performed.']}
    save(args.output/'evaluation-run.json', manifest)
    try:
        for arm in manifest['arms']:
            print(f'Starting {arm}: {len(rows)} frozen cases', flush=True)
            subprocess.run([sys.executable, '-u', str(Path(__file__).resolve()),
                            '--arm', arm, '--model', str(args.model), '--run', str(args.run),
                            '--reference', str(args.reference), '--output', str(args.output),
                            '--context', str(args.context), '--max-tokens', str(args.max_tokens)], check=True)
        manifest['metrics'] = {arm: json.loads((args.output/f'{arm}.json').read_text())['metrics'] for arm in manifest['arms']}
        manifest['status'] = 'completed'
    except BaseException as exc:
        manifest.update(status='failed', error=str(exc))
        raise
    finally:
        manifest['finished_at'] = datetime.now(timezone.utc).isoformat()
        save(args.output/'evaluation-run.json', manifest)
    print(json.dumps(manifest['metrics'], indent=2), flush=True)


if __name__ == '__main__':
    main()
