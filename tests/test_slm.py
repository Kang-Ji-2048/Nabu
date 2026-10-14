import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from nabu.slm import build_dataset, evaluate_baseline, ollama_completion


def frozen():
    item = {"id": "root", "source_key": "E-1", "created_at": "2020-01-01T00:00:00Z", "fields": {"title": "Plan", "description": None}, "unknown_fields": []}
    return {"plan": {"root": item, "members": [], "as_of": "2020-01-01T00:00:00Z"}, "corpus": {}, "evidence_fingerprint": "test"}


class SlmTests(unittest.TestCase):
    def test_external_baseline_keeps_identity_and_mixed_train_fails_before_inference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root/'external.jsonl'
            case = {'id': 'external', 'split': 'external_test',
                    'input': {'plan': frozen()['plan'], 'prior_work': [], 'allowed_risk_types': ['scope_gap']}}
            path.write_text(json.dumps(case))
            report = evaluate_baseline(path, root/'baseline.json', model='base-8b', checkpoint='Qwen/Qwen3-8B',
                                       completion=lambda *args: {'risks': [], 'limitations': []})
            self.assertEqual(report['expected_base_checkpoint'], 'Qwen/Qwen3-8B')
            self.assertFalse(report['trained'])
            path.write_text(json.dumps(case)+'\n'+json.dumps({**case, 'id': 'train', 'split': 'train'}))
            with patch('nabu.slm.ollama_completion') as inference:
                with self.assertRaisesRegex(ValueError, 'only validation/test/external_test'):
                    evaluate_baseline(path, root/'bad.json', model='base-8b')
                inference.assert_not_called()
            self.assertFalse((root/'bad.json').exists())

    def test_review_gate_and_empty_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases = root / "cases.jsonl"
            case = {"id": "one", "epic": "E-1", "as_of": "2020-01-01", "target": {"risks": [], "limitations": ["Insufficient evidence"]}}
            cases.write_text(json.dumps(case))
            with patch("nabu.slm.freeze_evidence", return_value=frozen()):
                with self.assertRaisesRegex(ValueError, "human reviewer"):
                    build_dataset(root / "db", cases, root / "out", train_before="2021-01-01", eval_before="2022-01-01", risk_types=["scope_gap"])
                case.update(review_status="approved", reviewer="Reviewer")
                cases.write_text(json.dumps(case))
                result = build_dataset(root / "db", cases, root / "out", train_before="2021-01-01", eval_before="2022-01-01", risk_types=["scope_gap"])
            self.assertEqual(result["approved"], 1)
            row = json.loads((root / "out/train.jsonl").read_text())
            self.assertEqual(row["messages"][-1]["role"], "assistant")

    def test_related_group_cannot_cross_time(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases = root / "cases"
            cases.write_text('\n'.join(json.dumps({"id": str(i), "epic": "E-1", "as_of": date}) for i, date in enumerate(["2020-01-01", "2023-01-01"])))
            first, second = frozen(), frozen()
            second["plan"]["as_of"] = "2023-01-01T00:00:00Z"
            with patch("nabu.slm.freeze_evidence", side_effect=[first, second]):
                with self.assertRaisesRegex(ValueError, "crosses time"):
                    build_dataset(root / "db", cases, root / "out", train_before="2021-01-01", eval_before="2022-01-01", risk_types=["scope_gap"])
            self.assertFalse((root / "out").exists())

    def test_baseline_zero_findings_and_invalid_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dataset = root / "dataset"
            dataset.write_text(json.dumps({"id": "one", "split": "test", "input": {"plan": frozen()["plan"], "prior_work": [], "allowed_risk_types": ["scope_gap"]}}))
            report = evaluate_baseline(dataset, root / "report", model="base", completion=lambda *args: {"risks": [], "limitations": []})
            self.assertFalse(report["trained"])
            self.assertIsNone(report["metrics"]["citation_valid_finding_fraction"])
            self.assertIsNone(report["metrics"]["false_alarms"])
            bad = evaluate_baseline(dataset, root / "bad", model="base", completion=lambda *args: {"unexpected": True})
            self.assertEqual(bad["metrics"]["schema_valid_cases"], 0)

    def test_invalid_citations_and_disallowed_types_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dataset = root / "dataset"
            payload = {"plan": frozen()["plan"], "prior_work": [], "allowed_risk_types": ["scope_gap"]}
            dataset.write_text(json.dumps({"id": "one", "split": "test", "input": payload}))
            risk = {"id": "risk", "risk_type": "scope_gap", "claim": "Possible gap", "rationale": "Compare prior evidence",
                    "suggested_action": "Check scope", "target_item_ids": ["root"], "severity": "low",
                    "citations": [{"item_id": key, "field": "title", "quote": "invented"} for key in ("one", "two")]}
            report = evaluate_baseline(dataset, root / "report", model="base",
                                       completion=lambda *args: {"risks": [risk], "limitations": []})
            self.assertEqual(report["metrics"]["citation_valid_finding_fraction"], 0)
            self.assertTrue(report["results"][0]["citation_errors"])

    def test_budget_fails_before_network(self):
        with patch("nabu.slm.LocalSLM") as request:
            with self.assertRaisesRegex(ValueError, "byte budget"):
                ollama_completion("http://localhost:11434/v1", "base", [], 1, 10)
            request.assert_not_called()
