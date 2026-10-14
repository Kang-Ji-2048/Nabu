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
