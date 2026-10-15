from contextlib import closing
import hashlib
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from nabu.labelling import signals, write_weak_labels
from nabu.pipeline import load
from nabu.risk.classifier import CHOICES, RUBRICS, JevClassifier, classify_dataset, validate_result
from nabu.risk.label_evidence import classifier_payload


class Teacher:
    def __init__(self, fail_on=None):
        self.inputs = []
        self.fail_on = fail_on

    def classify(self, payload):
        self.inputs.append(payload)
        if len(self.inputs) == self.fail_on:
            raise RuntimeError("Service failed")
        return {risk: {"choice": "risk", "confidence": 0.9,
                       "evidence": payload.get("snippets", [])[:1], "evidence_confidence": 0.9,
                       "probabilities": {"risk": 0.9, "no_risk": 0.05, "insufficient_evidence": 0.05}}
                for risk in RUBRICS}


class LabellingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.db = self.root / "source.sqlite"
        load(Path("tests/fixtures/tawos-synthetic.jsonl"), self.db)
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute("INSERT INTO event VALUES ('reopen','tawos-v1.1:10','2021-01-08T00:00:00.000000Z','status_changed','status','Done','Reopened',NULL,NULL)")
            c.execute("INSERT INTO event VALUES ('block','tawos-v1.1:10','2021-02-01T00:00:00.000000Z','status_changed','status','Open','Blocked',NULL,NULL)")
            c.execute("INSERT INTO event VALUES ('title','tawos-v1.1:10','2021-01-08T00:00:00.000000Z','text_changed','summary','Original migration','FUTURE_SECRET',NULL,NULL)")
        self.dataset = self.root / "dataset"

    def export(self):
        return write_weak_labels(self.db, "DEMO", "2021-01-03", "2021-01-20", self.dataset)

    def test_labels_link_to_events_and_exclude_future_input(self):
        report = self.export()
        self.assertEqual(report["counts"]["estimation"], 1)
        self.assertEqual(report["counts"]["rework"], 1)
        self.assertNotIn("dependency", report["counts"])
        self.assertEqual(report["excluded"]["no_recoverable_text"], 1)
        inputs = (self.dataset / "inputs.jsonl").read_text()
        self.assertNotIn("FUTURE_SECRET", inputs)
        self.assertNotIn("Reopened", inputs)
        labels = json.loads((self.dataset / "labels.jsonl").read_text())
        self.assertEqual(labels["targets"], {"estimation": 1, "rework": 1, "dependency": None})
        self.assertEqual({e["item_id"] for e in labels["evidence"]}, {labels["item_id"]})
        for name, digest in report["files"].items():
            self.assertEqual(hashlib.sha256((self.dataset / name).read_bytes()).hexdigest(), digest)

    def test_no_signal_is_unlabelled_and_output_is_reproducible(self):
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute("DELETE FROM event WHERE field IN ('status','Story Points')")
        first = self.export()
        rows = [json.loads(line) for line in (self.dataset / "labels.jsonl").read_text().splitlines()]
        self.assertTrue(all(row["state"] == "no_observed_signal" for row in rows))
        self.assertTrue(all(value is None for row in rows for value in row["targets"].values()))
        other = write_weak_labels(self.db, "DEMO", "2021-01-03", "2021-01-20", self.root / "other")
        self.assertEqual(first["dataset_sha256"], other["dataset_sha256"])
        with self.assertRaisesRegex(ValueError, "new or empty"):
            self.export()

    def test_invalid_window_and_actual_effort_never_labelled(self):
        with self.assertRaisesRegex(ValueError, "later"):
            write_weak_labels(self.db, "DEMO", "2021-02-01", "2021-01-01", self.dataset)
        event = {"field": "Actual Story Points", "from_value": "1", "to_value": "10"}
        self.assertEqual(signals(event), [])
        for value in ("NaN", "inf", "-1", "bad", None):
            self.assertEqual(signals({**event, "field": "Story Points", "to_value": value, "to_id": None}), [])

    def test_classifier_resumes_and_never_sees_outcomes(self):
        # Make both tickets' historical text recoverable.
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute("UPDATE work_item SET updated_at=created_at WHERE source_key='DEMO-2'")
        self.export()
        teacher = Teacher(fail_on=2)
        output = self.root / "predictions"
        with self.assertRaises(RuntimeError):
            classify_dataset(self.dataset, output, "test-jev", classifier=teacher)
        resumed = Teacher()
        report = classify_dataset(self.dataset, output, "test-jev", classifier=resumed)
        self.assertEqual(len(resumed.inputs), 1)
        self.assertEqual(report["classified"], 2)
        self.assertEqual(report["training_examples"], 2)
        training = [json.loads(line) for line in (output / "training.jsonl").read_text().splitlines()]
        self.assertEqual(len(training), 2)
        self.assertEqual(set(training[0]["targets"]), set(RUBRICS))
        for payload in teacher.inputs + resumed.inputs:
            self.assertIn("documents", payload)
            self.assertIn("snippets", payload)
            self.assertNotIn("targets", payload)
            self.assertNotIn("FUTURE_SECRET", json.dumps(payload))
        done = Teacher()
        classify_dataset(self.dataset, output, "test-jev", classifier=done)
        self.assertEqual(done.inputs, [])
        with self.assertRaisesRegex(ValueError, "Cannot change"):
            classify_dataset(self.dataset, output, "other", classifier=done)

    def test_abstention_validation_and_input_tampering(self):
        answers = Teacher().classify({})
        answers["rework"]["confidence"] = 0.5
        answers["dependency"]["choice"] = "insufficient_evidence"
        result = validate_result(answers, 0.8)
        self.assertIsNone(result["rework"]["target"])
        self.assertIsNone(result["dependency"]["target"])
        self.assertEqual(result["estimation"]["target"], 1)
        answers["estimation"]["confidence"] = float("nan")
        with self.assertRaises(ValueError):
            validate_result(answers, 0.8)
        self.export()
        with (self.dataset / "inputs.jsonl").open("a") as stream:
            stream.write("{}\n")
        with self.assertRaisesRegex(ValueError, "hash"):
            classify_dataset(self.dataset, self.root / "predictions", "test", classifier=Teacher())

    def test_official_sdk_adapter_without_network(self):
        try:
            from typesafe_sdk import SystemOneResponse
        except ImportError:
            self.skipTest("Optional Jev SDK is not installed")
        self.export()
        payload = classifier_payload(json.loads((self.dataset / "inputs.jsonl").read_text()))
        evidence_id = payload["snippets"][0]["evidence_id"]
        answers = {risk: {"type": "choice", **{k: v for k, v in answer.items() if k in {"choice", "confidence", "probabilities"}}}
                   for risk, answer in Teacher().classify({}).items()}
        response = SystemOneResponse.model_validate({"model": "resolved-jev", "usage": {}, "answers": answers})
        evidence = SystemOneResponse.model_validate({"model": "resolved-jev", "usage": {},
            "answers": {risk: {"type": "choice", "choice": evidence_id, "confidence": 0.95,
                               "probabilities": {"none": 0.05, evidence_id: 0.95}} for risk in RUBRICS}})
        with patch.dict("os.environ", {"TYPESAFE_API_KEY": "test-key"}), \
             patch("typesafe_sdk.TypeSafeClient") as client_type:
            client = client_type.return_value
            client.system_one.side_effect = [response, evidence]
            adapter = JevClassifier("test-jev")
            result = adapter.classify(payload)
            self.assertEqual(adapter.served_model, "resolved-jev")
            self.assertTrue(all(v["target"] == 1 for v in validate_result(result, 0.8, payload).values()))
            request = client.system_one.call_args.kwargs
            self.assertEqual(set(request["questions"]), set(RUBRICS))
            self.assertEqual(request["state"], payload)
            adapter.close()
            client.close.assert_called_once()

    def test_historical_acceptance_and_epic_context_exclude_future_values(self):
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute("UPDATE work_item SET updated_at=created_at WHERE source_key='DEMO-2'")
            c.execute("INSERT INTO event VALUES ('criteria','tawos-v1.1:10','2021-01-08T00:00:00.000000Z','text_changed','Acceptance Criteria','Must support migration rollback.','SECRET_CRITERIA',NULL,NULL)")
            c.execute("INSERT INTO event VALUES ('member','tawos-v1.1:10','2021-01-02T00:00:00.000000Z','membership_changed','Epic Child',NULL,'DEMO-2',NULL,NULL)")
        report = self.export()
        rows = [json.loads(line) for line in (self.dataset / "inputs.jsonl").read_text().splitlines()]
        child = next(r for r in rows if r["input"]["ticket"]["source_key"] == "DEMO-2")
        self.assertIn("Must support migration rollback.", json.dumps(child))
        self.assertNotIn("SECRET", json.dumps(child))
        self.assertEqual(report["profile"]["tickets_with_plan_context"], 2)
        self.assertEqual(child["group_item_ids"], ["tawos-v1.1:10", "tawos-v1.1:11"])
        self.assertEqual(child["input"]["context"]["dependencies"], "unknown_snapshot_links_excluded")

    def test_forged_and_unknown_evidence_abstain(self):
        self.export()
        payload = classifier_payload(json.loads((self.dataset / "inputs.jsonl").read_text()))
        answers = Teacher().classify(payload)
        answers["scope_gap"]["evidence"] = [{**payload["snippets"][0], "quote": "Fabricated"}]
        result = validate_result(answers, 0.8, payload)
        self.assertIsNone(result["scope_gap"]["target"])
        self.assertIn("missing_or_invalid_evidence", result["scope_gap"]["abstention_reasons"])
        self.assertEqual(result["rework"]["target"], 1)

    def test_xd_review_stage_and_initial_zero_estimate_are_not_outcomes(self):
        self.assertEqual(signals({"field": "status", "from_value": "In Progress", "to_value": "In PR"}), [])
        self.assertEqual(signals({"field": "Story Points", "from_value": "0", "to_value": "5"}), [])


if __name__ == "__main__":
    unittest.main()
