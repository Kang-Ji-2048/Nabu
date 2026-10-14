"""Record review provenance without treating assistant review as human approval."""
import hashlib
import json


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def review_kind(row):
    reviewer = row.get('reviewer')
    if not isinstance(reviewer, str) or not reviewer.strip():
        raise ValueError('Reviewed labels require a named reviewer')
    kind = row.get('reviewer_kind', 'human')
    expected = {'human': 'approved', 'assistant': 'assistant_reviewed'}.get(kind)
    if expected is None or row.get('review_status') != expected:
        raise ValueError('Review status must match human or assistant reviewer provenance')
    review = row.get('review')
    if kind == 'assistant' and not isinstance(review, dict):
        raise ValueError('Assistant review requires a record bound to input and target')
    if review is not None:
        if (review.get('reviewer') != reviewer.strip() or review.get('reviewer_kind') != kind
                or review.get('action') not in {'approve', 'revise'}):
            raise ValueError('Review record does not match reviewer/action')
        for key in ('reason', 'reviewed_at'):
            if not isinstance(review.get(key), str) or not review[key].strip():
                raise ValueError(f'Review record requires {key}')
        if review.get('input_sha256') != digest(row['input']) or review.get('target_sha256') != digest(row['target']):
            raise ValueError('Input or target changed after review')
    if kind == 'assistant' and row.get('human_approved') is not False:
        raise ValueError('Assistant review cannot claim human approval')
    if kind == 'assistant':
        if row.get('labelling_questions'):
            raise ValueError('Assistant review still has pending labelling questions')
        questions = row.get('candidate_labelling_questions', [])
        resolutions = review.get('question_resolutions', [])
        if [item.get('question') for item in resolutions] != questions:
            raise ValueError('Every candidate question requires an explicit review disposition')
        for item in resolutions:
            if item.get('disposition') not in {'answered_from_supplied_input', 'accepted_as_limitation'} or not isinstance(item.get('resolution'), str) or not item['resolution'].strip():
                raise ValueError('Question resolution requires a supported answer or explicit retained limitation')
    return kind


def review_summary(rows):
    kinds = set()
    for row in rows:
        if row.get('review_status') == 'generated_unreviewed':
            kinds.add('unreviewed_machine')
        else:
            kinds.add(review_kind(row))
    label = {'human': 'human_reviewed', 'assistant': 'assistant_reviewed',
             'unreviewed_machine': 'unreviewed_machine_labels'}
    return {'label_review': label[next(iter(kinds))] if len(kinds) == 1 else 'mixed_review_provenance',
            'reviewer_kinds': sorted(kinds), 'label_review_complete': 'unreviewed_machine' not in kinds,
            'human_approved': kinds == {'human'}, 'experimental': kinds != {'human'}}


def evaluation_coverage(train, validation):
    allowed = sorted({kind for row in train + validation for kind in row['input']['allowed_risk_types']})
    counts = {}
    for split, rows in (('train', train), ('validation', validation)):
        counts[split] = {kind: sum(risk['risk_type'] == kind for row in rows for risk in row['target']['risks']) for kind in allowed}
    positives = sum(bool(row['target']['risks']) for row in validation)
    warnings = []
    if not positives:
        warnings.append('Validation has no positive reference risks; recall is undefined.')
    missing = [kind for kind in allowed if not counts['train'][kind]]
    if missing:
        warnings.append('No positive training examples for: ' + ', '.join(missing))
    return {'positive_findings_by_type': counts, 'validation_positive_examples': positives,
            'risk_recall_estimable': bool(positives), 'missing_positive_training_types': missing,
            'production_quality_verified': False, 'warnings': warnings}
