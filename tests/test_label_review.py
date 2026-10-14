from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from nabu.label_review import digest, evaluation_coverage, review_kind, review_summary

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('review_training', ROOT/'scripts/train-slm-mlx.py')
training = importlib.util.module_from_spec(spec)
spec.loader.exec_module(training)


def reviewed(split='train'):
    row = {'id': split, 'split': split, 'group': split, 'epic': split,
           'input': {'plan': {'root': {'id': split}, 'members': []}, 'prior_work': [],
                     'allowed_risk_types': ['scope_gap', 'validation_gap']},
           'target': {'risks': [], 'limitations': ['Insufficient supplied evidence']},
           'review_status': 'assistant_reviewed', 'reviewer': 'Codex', 'reviewer_kind': 'assistant', 'human_approved': False}
    row['review'] = {'reviewer': 'Codex', 'reviewer_kind': 'assistant', 'action': 'approve',
                     'reason': 'Reviewed this frozen example without predictions', 'reviewed_at': '2026-10-14T20:00:00Z',
                     'input_sha256': digest(row['input']), 'target_sha256': digest(row['target'])}
    return row


class ReviewProvenanceTests(unittest.TestCase):
    def test_assistant_reviews_remain_experimental_not_human(self):
        row = reviewed()
        self.assertEqual(review_kind(row), 'assistant')
        result = review_summary([row])
        self.assertTrue(result['label_review_complete'])
        self.assertTrue(result['experimental'])
        self.assertFalse(result['human_approved'])
        self.assertEqual(result['label_review'], 'assistant_reviewed')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'train.jsonl'
            path.write_text(json.dumps(row))
            self.assertEqual(training.read_partition(path, 'train')[0]['reviewer_kind'], 'assistant')

    def test_review_cannot_follow_edited_input_or_target(self):
        for field in ('input', 'target'):
            row = reviewed()
            row[field]['edited'] = True
            with self.assertRaisesRegex(ValueError, 'changed after review'):
                review_kind(row)

    def test_assistant_cannot_claim_human_approval_or_omit_seal(self):
        for change in ({'human_approved': True}, {'review_status': 'approved'}, {'review': None}):
            with self.subTest(change=change):
                row = {**reviewed(), **change}
                with self.assertRaises(ValueError):
                    review_kind(row)

    def test_pending_questions_require_explicit_disposition_without_inventing_unknowns(self):
        row = reviewed()
        question = 'What are the unknown deployment acceptance criteria?'
        row['labelling_questions'] = [question]
        with self.assertRaisesRegex(ValueError, 'pending labelling questions'):
            review_kind(row)
        row['candidate_labelling_questions'] = row.pop('labelling_questions')
        with self.assertRaisesRegex(ValueError, 'explicit review disposition'):
            review_kind(row)
        row['review']['question_resolutions'] = [{'question': question, 'disposition': 'accepted_as_limitation',
                                                'resolution': 'The supplied input does not recover them; retain unknown scope and the no-supported-risk target.'}]
        self.assertEqual(review_kind(row), 'assistant')

    def test_zero_validation_positives_never_report_recall_readiness(self):
        coverage = evaluation_coverage([reviewed()], [reviewed('validation')])
        self.assertFalse(coverage['risk_recall_estimable'])
        self.assertFalse(coverage['production_quality_verified'])
        self.assertEqual(coverage['missing_positive_training_types'], ['scope_gap', 'validation_gap'])

    def test_reviewed_split_cannot_change_audited_boundaries(self):
        row = reviewed('validation')
        row['as_of'] = '2020-01-01'
        row['input']['plan']['as_of'] = '2020-01-01T00:00:00Z'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'preparation.json'
            path.write_text(json.dumps({'version': 'nabu-training-preparation-v1', 'ready_for_training': True,
                                        'inputs': {row['id']: digest(row['input'])},
                                        'train_before': '2021-01-01', 'eval_before': '2022-01-01'}))
            with self.assertRaisesRegex(ValueError, 'audited time boundaries'):
                training.validate_preparation(path, [row])


class AssistantExportTests(unittest.TestCase):
    def test_export_rejects_stale_or_incomplete_decisions_then_preserves_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            rows = [reviewed(), reviewed('validation')]
            for row in rows:
                row['review_status'] = 'generated_unreviewed'
                for key in ('review', 'reviewer', 'reviewer_kind', 'human_approved'):
                    row.pop(key)
            rows[0]['labelling_questions'] = ['Which unknown acceptance criteria apply?']
            candidate = root/'candidates.jsonl'
            candidate.write_text(''.join(json.dumps(row)+'\n' for row in rows))
            manifest = root/'manifest.json'
            manifest.write_text(json.dumps({'version': 'nabu-training-preparation-v1', 'ready_for_training': True,
                                             'inputs': {row['id']: digest(row['input']) for row in rows}}))
            decisions = []
            for row in rows:
                decisions.append({'id': row['id'], 'action': 'approve', 'reviewer': 'Codex', 'reviewer_kind': 'assistant',
                                  'reason': 'No relevant supplied evidence', 'reviewed_at': '2026-10-14T20:00:00Z',
                                  'input_sha256': digest(row['input']), 'candidate_target_sha256': digest(row['target']),
                                  'target_sha256': digest(row['target'])})
                decisions[-1]['question_resolutions'] = [
                    {'question': question, 'disposition': 'accepted_as_limitation',
                     'resolution': 'Acceptance criteria are unavailable in the frozen input; retain that limitation without inventing a missing-work risk.'}
                    for question in row.get('labelling_questions', [])]
            path = root/'decisions.jsonl'
            output = root/'reviewed'
            def run(values):
                path.write_text(''.join(json.dumps(row)+'\n' for row in values))
                return subprocess.run([sys.executable, str(ROOT/'scripts/export-reviewed-slm.py'), '--candidates', str(candidate),
                                       '--decisions', str(path), '--preparation-manifest', str(manifest), '--output', str(output),
                                       '--reviewer-kind', 'assistant'], capture_output=True, text=True)
            self.assertIn('incomplete', run(decisions[:1]).stderr)
            stale = deepcopy(decisions)
            stale[0]['candidate_target_sha256'] = 'stale'
            self.assertIn('bind the candidate', run(stale).stderr)
            unresolved = deepcopy(decisions)
            unresolved[0]['question_resolutions'] = []
            self.assertIn('explicit review disposition', run(unresolved).stderr)
            self.assertFalse(output.exists())
            result = run(decisions)
            self.assertEqual(result.returncode, 0, result.stderr)
            exported = json.loads((output/'train.jsonl').read_text())
            self.assertEqual(exported['input'], rows[0]['input'])
            self.assertEqual(review_kind(exported), 'assistant')
            self.assertFalse(exported['human_approved'])
            self.assertEqual(exported['labelling_questions'], [])
            self.assertEqual(exported['candidate_labelling_questions'], rows[0]['labelling_questions'])
            summary = json.loads((output/'review-export.json').read_text())
            self.assertFalse(summary['human_approved'])
            self.assertTrue(summary['label_review_complete'])
