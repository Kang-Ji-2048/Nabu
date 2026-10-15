import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TrainingHandoffTests(unittest.TestCase):
    @unittest.skipIf(os.name == 'nt', 'POSIX training launcher requires Unix executable semantics')
    def test_preparation_script_never_starts_labelled_training(self):
        with tempfile.TemporaryDirectory(prefix='nabu handoff ') as directory:
            root = Path(directory)
            (root/'scripts').mkdir()
            shutil.copyfile(ROOT/'scripts/prepare-epoch1.sh', root/'scripts/prepare-epoch1.sh')
            (root/'data/models/qwen3-8b-mlx-4bit').mkdir(parents=True)
            (root/'data/training').mkdir()
            (root/'.venv-slm/bin').mkdir(parents=True)
            fake = root/'.venv-slm/bin/python'
            fake.write_text('#!/usr/bin/env python3\nimport json, os, sys\n'
                            "with open(os.environ['NABU_TEST_CALL_LOG'], 'a') as f: f.write(json.dumps(sys.argv[1:])+'\\n')\n"
                            "if any(x.endswith('train-slm-mlx.py') for x in sys.argv) and '--preflight-only' not in sys.argv: raise SystemExit(99)\n"
                            "print('{}')\n")
            fake.chmod(0o755)
            log = root/'calls.jsonl'
            result = subprocess.run(['bash', str(root/'scripts/prepare-epoch1.sh')], cwd=root.parent,
                                    env={**os.environ, 'NABU_TEST_CALL_LOG': str(log)}, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            calls = [json.loads(line) for line in log.read_text().splitlines()]
            train = [args for args in calls if any(x.endswith('train-slm-mlx.py') for x in args)]
            self.assertEqual(len(train), 1)
            self.assertIn('--preflight-only', train[0])
            self.assertIn('--base-revision', train[0])
            self.assertNotIn('mlx-slm-worker.py', json.dumps(calls))
            self.assertFalse(any(root.rglob('training-run.json')))
            self.assertFalse(any(root.rglob('unused-training-output')))

    def test_checked_packages_work_without_original_db_model_or_absolute_paths(self):
        with tempfile.TemporaryDirectory(prefix='nabu portable ') as directory:
            root = Path(directory)
            for name in ('nabu', 'scripts', 'data/training/xd-assistant-reviewed-v3',
                         'data/external-test/mesos-ai-reference-v1', 'data/external-test/mesos-roster-v1'):
                shutil.copytree(ROOT/name, root/name, ignore=shutil.ignore_patterns('__pycache__'))
            for script, key in (('check-reviewed-data.py', 'data_ready_for_experiment'),
                                ('check-external-reference.py', 'external_reference_ready')):
                result = subprocess.run([sys.executable, '-B', str(root/'scripts'/script)],
                                        cwd=root.parent, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(json.loads(result.stdout)[key])
            # Even a valid JSON edit must fail the portable package inventory.
            path = root/'data/training/xd-assistant-reviewed-v3/train.jsonl'
            path.write_text(path.read_text()+'\n')
            result = subprocess.run([sys.executable, '-B', str(root/'scripts/check-reviewed-data.py')],
                                    cwd=root.parent, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('file changed', result.stderr)
