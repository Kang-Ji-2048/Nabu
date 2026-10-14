"""Draft local Qwen risk labels; preserve machine provenance and the test holdout."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.slm import messages
from nabu.risk.contracts import Detection
from nabu.risk.runner import validate_detection


def parse_response(text):
    text = text.strip()
    if text.startswith('```') and text.endswith('```'):
        text = text.split('\n', 1)[1].rsplit('```', 1)[0].strip()
    detection = Detection.model_validate_json(text).model_dump()
    return detection


def write_review(rows, path):
    lines = ['# Nabu generated risk labels for review', '', 'These labels are unreviewed machine suggestions. Schema and exact-quote checks establish format and provenance, not usefulness or correctness. Test cases are excluded.', '']
    for row in rows:
        plan = row['input']['plan']
        lines.extend([f"## {row['epic']} ({row['split']})", '', f"Historical cutoff: {row['as_of']}", '',
                      'Plan root:', '', '```json', json.dumps(plan['root'], ensure_ascii=False, indent=2), '```', '',
                      f"Observed members: {len(plan['members'])}; supplied prior tickets: {len(row['input']['prior_work'])}.", '',
                      'Proposed target:', '', '```json', json.dumps(row['target'], ensure_ascii=False, indent=2), '```', '',
                      'Review: approve, revise, or reject. Check comparability, missing fields, false alarms and useful next actions.', ''])
        lines.extend(['Supplied historical evidence:', '', '```json', json.dumps(row['input']['prior_work'], ensure_ascii=False, indent=2), '```', ''])
    path.write_text('\n'.join(lines) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, required=True)
    parser.add_argument('--model-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--max-tokens', type=int, default=2048)
    args = parser.parse_args()
    provenance = json.loads((args.model_dir / 'nabu-base.json').read_text())
    rows = []
    for split in ('train', 'validation'):
        rows.extend(json.loads(line) for line in (args.dataset / f'{split}-drafts.jsonl').read_text().splitlines() if line.strip())
    if any(row['split'] not in {'train', 'validation'} for row in rows):
        raise ValueError('Test examples cannot enter label generation for training')
    args.output.mkdir(parents=True, exist_ok=True)
    completed_path = args.output / 'generated-labels.jsonl'
    existing = [json.loads(line) for line in completed_path.read_text().splitlines()] if completed_path.exists() else []
    completed = {row['id'] for row in existing}
    write_review(existing, args.output / 'review.md')
    from mlx_lm import load, generate
    from mlx_lm.sample_utils import make_sampler
    model, tokenizer = load(str(args.model_dir))
    schema = json.dumps(Detection.model_json_schema())
    with completed_path.open('a') as output, (args.output / 'label-events.jsonl').open('a') as events:
        for row in rows:
            if row['id'] in completed:
                continue
            conversation = messages(row['input'])
            conversation[0]['content'] += '\nReturn only JSON conforming to this schema: ' + schema
            accepted = None
            for attempt in range(2):
                prompt = tokenizer.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True, enable_thinking=False)
                response = generate(model, tokenizer, prompt=prompt, max_tokens=args.max_tokens, sampler=make_sampler(temp=0), verbose=False)
                try:
                    candidate = parse_response(response)
                    validated = validate_detection(candidate, row['input'])
                    if validated['rejected']:
                        raise ValueError(str(validated['rejected']))
                    accepted = candidate
                    break
                except ValueError as exc:
                    events.write(json.dumps({'id': row['id'], 'attempt': attempt + 1, 'status': 'rejected', 'reason': str(exc), 'response': response}) + '\n')
                    events.flush()
                    conversation = messages(row['input'])
                    conversation[0]['content'] += '\nReturn only JSON conforming to this schema: ' + schema
                    conversation[0]['content'] += '\nA previous answer failed validation: ' + str(exc) + '. Recheck exact quotes; do not invent citations or force a warning.'
            if accepted is None:
                print(json.dumps({'id': row['id'], 'status': 'label_failed'}), flush=True)
                continue
            labelled = {**row, 'target': accepted, 'review_status': 'generated_unreviewed',
                        'label_source': {'kind': 'local_model', **provenance}, 'label_validation': 'schema_and_citations_only'}
            output.write(json.dumps(labelled, ensure_ascii=False) + '\n')
            output.flush()
            existing.append(labelled)
            write_review(existing, args.output / 'review.md')
            print(json.dumps({'id': row['id'], 'status': 'generated_unreviewed', 'risk_count': len(accepted['risks'])}), flush=True)
    print('Generated labels require human review unless an explicitly experimental run is requested.', flush=True)


if __name__ == '__main__':
    main()
