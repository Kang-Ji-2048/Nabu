import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('nabu_mlx_training', Path(__file__).resolve().parents[1] / 'scripts/train-slm-mlx.py')
training = importlib.util.module_from_spec(spec)
spec.loader.exec_module(training)


class TrainingGateTests(unittest.TestCase):
    def test_generated_labels_cannot_pass_human_review_gate(self):
        row = {'id': 'example', 'split': 'train', 'review_status': 'generated_unreviewed',
               'label_source': {'kind': 'local_model'}, 'target': {'risks': [], 'limitations': []},
               'input': {'plan': {'root': {'id': 'root'}, 'members': []}, 'prior_work': [], 'allowed_risk_types': ['scope_gap']}}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'train.jsonl'
            path.write_text(json.dumps(row))
            with self.assertRaisesRegex(ValueError, 'human reviews'):
                training.read_partition(path, 'train')
            accepted = training.read_partition(path, 'train', allow_generated=True)
            self.assertEqual(accepted[0]['review_status'], 'generated_unreviewed')
            self.assertNotIn('reviewer', accepted[0])
            with self.assertRaisesRegex(ValueError, 'human reviews'):
                training.read_partition(path, 'validation', allow_generated=True)

    def test_approved_labels_require_named_reviewer(self):
        row = {'id': 'example', 'split': 'train', 'review_status': 'approved', 'reviewer': '  '}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'train.jsonl'
            path.write_text(json.dumps(row))
            with self.assertRaisesRegex(ValueError, 'human reviews'):
                training.read_partition(path, 'train')


class PreparationAuditGateTests(unittest.TestCase):
    def test_training_requires_matching_audited_inputs(self):
        import hashlib
        row = {'id': 'example', 'input': {'plan': {'root': {'id': 'root'}}}}
        with self.assertRaisesRegex(ValueError, 'preparation-manifest'):
            training.validate_preparation(None, [row])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'preparation.json'
            digest = hashlib.sha256(json.dumps(row['input'], sort_keys=True, ensure_ascii=False).encode()).hexdigest()
            manifest = {'version': 'nabu-training-preparation-v1', 'ready_for_training': False, 'inputs': {'example': digest}}
            path.write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, 'not ready'):
                training.validate_preparation(path, [row])
            manifest['ready_for_training'] = True
            path.write_text(json.dumps(manifest))
            self.assertTrue(training.validate_preparation(path, [row])['ready_for_training'])
            row['input']['plan']['root']['id'] = 'edited'
            with self.assertRaisesRegex(ValueError, 'differs'):
                training.validate_preparation(path, [row])

    def test_preflight_can_inspect_candidates_without_approving_them(self):
        row = {'id': 'example', 'split': 'train', 'review_status': 'generated_unreviewed',
               'label_source': {'kind': 'assistant_generated'}, 'target': {'risks': [], 'limitations': []},
               'input': {'plan': {'root': {'id': 'root'}, 'members': []}, 'prior_work': [], 'allowed_risk_types': ['scope_gap']}}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'train.jsonl'
            path.write_text(json.dumps(row))
            inspected = training.read_partition(path, 'train', inspect_only=True)
            self.assertEqual(inspected[0]['review_status'], 'generated_unreviewed')
            with self.assertRaisesRegex(ValueError, 'human reviews'):
                training.read_partition(path, 'train')
            path.write_text(json.dumps(row)+'\n'+json.dumps(row))
            with self.assertRaisesRegex(ValueError, 'Duplicate'):
                training.read_partition(path, 'train', inspect_only=True)


class HumanReviewExportTests(unittest.TestCase):
    def test_pending_review_cannot_export_and_explicit_review_preserves_inputs(self):
        import hashlib
        import subprocess
        import sys
        root_path = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            candidates = []
            for split in ('train', 'validation'):
                candidates.append({'id': split, 'epic': split, 'group': split, 'split': split,
                                   'input': {'plan': {'root': {'id': split}, 'members': []}, 'prior_work': [], 'allowed_risk_types': ['scope_gap']},
                                   'target': {'risks': [], 'limitations': ['Synthetic fixture']},
                                   'review_status': 'generated_unreviewed', 'label_source': {'kind': 'assistant_generated'}})
            candidate_path = root/'candidates.jsonl'
            candidate_path.write_text(''.join(json.dumps(r)+'\n' for r in candidates))
            manifest_path = root/'manifest.json'
            manifest_path.write_text(json.dumps({'version': 'nabu-training-preparation-v1', 'ready_for_training': True,
                                                'inputs': {r['id']: hashlib.sha256(json.dumps(r['input'],sort_keys=True,ensure_ascii=False).encode()).hexdigest() for r in candidates}}))
            decisions_path = root/'decisions.jsonl'
            output = root/'approved'
            def run():
                return subprocess.run([sys.executable, str(root_path/'scripts/export-reviewed-slm.py'), '--candidates', str(candidate_path),
                                       '--decisions', str(decisions_path), '--preparation-manifest', str(manifest_path), '--output', str(output)], capture_output=True,text=True)
            decisions = [{'id': r['id'], 'action': 'pending', 'reviewer': 'Synthetic test reviewer'} for r in candidates]
            decisions_path.write_text(''.join(json.dumps(r)+'\n' for r in decisions))
            blocked = run()
            self.assertNotEqual(blocked.returncode, 0)
            self.assertFalse(output.exists())
            for row in decisions:
                row['action'] = 'approve'
            decisions_path.write_text(''.join(json.dumps(r)+'\n' for r in decisions))
            self.assertEqual(run().returncode,0)
            exported = json.loads((output/'train.jsonl').read_text())
            self.assertEqual(exported['input'],candidates[0]['input'])
            self.assertEqual(exported['review_status'],'approved')
            self.assertEqual(exported['label_source'],candidates[0]['label_source'])
