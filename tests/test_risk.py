import json
from contextlib import closing
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from nabu.classification import classify
from nabu.pipeline import load
from nabu.risk.contracts import Detection
from nabu.risk.models import LocalSLM
from nabu.risk.runner import read_manifest, run_assessment, validate_detection, validate_presentation

CUTOFF = "2014-01-05T12:00:00Z"


class Detector:
    def __init__(self, invalid=False):
        self.calls = 0
        self.payload = None
        self.invalid = invalid

    def detect(self, payload):
        self.calls += 1
        self.payload = payload
        evidence = payload["prior_work"][:2]
        return {"risks": [{"id": "risk-1", "risk_type": "compatibility",
                           "claim": "Deployment compatibility may need verification.",
                           "rationale": "Both earlier module tasks include compatibility tests.",
                           "suggested_action": "Confirm compatibility test coverage.", "severity": "medium",
                           "target_item_ids": [payload["plan"]["root"]["id"]],
                           "citations": [{"item_id": item["id"], "field": "title",
                                          "quote": "Fabricated quote" if self.invalid else item["fields"]["title"]}
                                         for item in evidence]}], "limitations": ["Incomplete historical scope."]}


class Reporter:
    def __init__(self, fail=False):
        self.calls = 0
        self.payload = None
        self.fail = fail

    def present(self, payload):
        self.calls += 1
        self.payload = payload
        if self.fail:
            raise RuntimeError("Simulated service outage")
        return {"sections": [{"risk_id": risk["id"], "title": "Verify deployment compatibility",
                              "explanation": "Earlier module work included compatibility checks.",
                              "recommended_action": "Confirm whether these checks are covered."}
                             for risk in payload["risks"]]}


class RiskTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.database = self.root / "source.sqlite"
        rows = [{"table": "Project", "row": {"ID": 1, "Project_Key": "TEST"}}]
        for iid, key, title, created, updated in [
            (1, "TEST-1", "FUTURE_SECRET", "2014-01-01", "2014-02-01"),
            (2, "TEST-2", "Module deployment compatibility tests", "2013-01-01", "2013-01-02"),
            (3, "TEST-3", "Package module compatibility verification", "2013-01-01", "2013-01-02"),
            (4, "TEST-4", "FUTURE_SECRET", "2014-02-01", "2014-02-01"),
        ]:
            rows.append({"table": "Issue", "row": {"ID": iid, "Project_ID": 1, "Issue_Key": key,
                         "Title": title, "Description": "Module packaging.", "Type": "Task",
                         "Creation_Date": created, "Last_Updated": updated, "Status": "Done"}})
        rows.append({"table": "Change_Log", "row": {"ID": 100, "Issue_ID": 1, "Field": "summary",
                     "Creation_Date": "2014-02-01", "From_String": "Deploy custom module package",
                     "To_String": "FUTURE_SECRET"}})
        self.input = self.root / "input.jsonl"
        self.input.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
        load(self.input, self.database)
        self.manifest = self.root / "manifest.json"
        self.manifest_data = {"version": "nabu-slm-v1", "model": "test-trained-model", "trained": True,
                              "trained_through": "2013-12-01T00:00:00Z", "training_data_sha256": "a" * 64,
                              "artifact_sha256": "b" * 64, "risk_types": ["compatibility"]}
        self.manifest.write_text(json.dumps(self.manifest_data), encoding="utf-8")

    def run_live(self, detector, reporter, **options):
        return run_assessment(self.database, "TEST-1", CUTOFF, self.root / "run",
                              manifest_path=self.manifest, claude_model="test-claude", detector=detector,
                              reporter=reporter, **options)

    def test_classification_persists_and_refreshes_with_ingestion(self):
        with closing(sqlite3.connect(self.database)) as c:
            self.assertEqual(c.execute("SELECT COUNT(*) FROM work_classification").fetchone()[0], 4)
            self.assertEqual(c.execute("SELECT category FROM work_classification WHERE item_id=?",
                                      ("tawos-v1.1:3",)).fetchone()[0], "deployment")
        report = load(self.input, self.database)
        self.assertEqual(sum(report["work_categories"].values()), 4)
        with closing(sqlite3.connect(self.database)) as c:
            self.assertEqual(c.execute("SELECT COUNT(*) FROM work_classification").fetchone()[0], 4)
        self.assertEqual(classify("Unrecognised topic"), "unassigned")

    def test_slm_detection_precedes_claude_presentation(self):
        detector, reporter = Detector(), Reporter()
        report = self.run_live(detector, reporter)
        self.assertTrue(report["analysis_performed"])
        self.assertEqual(len(report["risks"]), 1)
        self.assertEqual(detector.calls, 1)
        self.assertEqual(reporter.calls, 1)
        self.assertEqual(reporter.payload["risks"], report["risks"])
        self.assertNotIn("FUTURE_SECRET", json.dumps(detector.payload))
        self.assertNotIn("outcome", detector.payload)
        self.assertTrue((self.root / "run/review.md").exists())
        self.assertIn("TEST-2", (self.root / "run/review.md").read_text(encoding="utf-8"))

    def test_fabricated_quotes_are_withheld_before_claude(self):
        reporter = Reporter()
        report = self.run_live(Detector(invalid=True), reporter)
        self.assertEqual(report["risks"], [])
        self.assertEqual(len(report["rejected"]), 1)
        self.assertEqual(reporter.calls, 0)

    def test_missing_training_is_not_silently_replaced(self):
        with self.assertRaisesRegex(ValueError, "trained SLM"):
            run_assessment(self.database, "TEST-1", CUTOFF, self.root / "run")
        self.assertFalse((self.root / "run").exists())
        self.manifest_data["trained"] = False
        self.manifest.write_text(json.dumps(self.manifest_data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "training is incomplete"):
            read_manifest(self.manifest, "2014-01-05T12:00:00.000000Z")

    def test_future_trained_model_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "training cutoff"):
            read_manifest(self.manifest, "2013-01-01T00:00:00.000000Z")

    def test_manifest_timestamp_offsets_are_normalised(self):
        self.manifest_data["trained_through"] = "2014-01-05T13:00:00+01:00"
        self.manifest.write_text(json.dumps(self.manifest_data), encoding="utf-8")
        self.assertEqual(read_manifest(self.manifest, "2014-01-05T12:00:00.000000Z")["trained_through"],
                         "2014-01-05T12:00:00.000000Z")

    def test_resume_after_claude_failure_does_not_repeat_slm(self):
        detector = Detector()
        with self.assertRaises(RuntimeError):
            self.run_live(detector, Reporter(fail=True))
        with closing(sqlite3.connect(self.database)) as c, c:
            c.execute("UPDATE work_item SET title='CHANGED_SECRET'")
        reporter = Reporter()
        report = run_assessment(None, None, None, self.root / "run", resume=True,
                                detector=detector, reporter=reporter)
        self.assertEqual(detector.calls, 1)
        self.assertNotIn("CHANGED_SECRET", json.dumps(reporter.payload))
        self.assertEqual(len(report["risks"]), 1)

    def test_completed_resume_needs_no_models_or_credentials(self):
        self.run_live(Detector(), Reporter())
        with patch("nabu.risk.runner.LocalSLM", side_effect=AssertionError("must not construct")), \
             patch("nabu.risk.runner.ClaudeReporter", side_effect=AssertionError("must not construct")):
            report = run_assessment(None, None, None, self.root / "run", resume=True)
        self.assertEqual(report["status"], "completed")

    def test_resume_rejects_changed_inputs(self):
        self.run_live(Detector(), Reporter(), pause_after_prepare=True)
        for kwargs in ({"epic": "OTHER"}, {"evidence_limit": 5}, {"slm_endpoint": "http://127.0.0.1:9000/v1"}):
            arguments = dict(database=None, epic=None, cutoff=None, run_dir=self.root / "run", resume=True)
            arguments.update(kwargs)
            with self.assertRaisesRegex(ValueError, "Cannot change"):
                run_assessment(**arguments)

    def test_offline_is_explicit_and_resumable(self):
        paused = run_assessment(self.database, "TEST-1", CUTOFF, self.root / "run", offline=True,
                                pause_after_prepare=True)
        self.assertEqual(paused["status"], "paused")
        report = run_assessment(None, None, None, self.root / "run", resume=True)
        self.assertFalse(report["analysis_performed"])
        self.assertEqual(report["risks"], [])
        self.assertIn("no AI analysis", (self.root / "run/review.md").read_text(encoding="utf-8"))

    def test_reporter_cannot_add_omit_or_duplicate_risks(self):
        risk = {"id": "risk-1"}
        section = {"risk_id": "invented", "title": "Title", "explanation": "Explanation", "recommended_action": "Action"}
        for sections in ([], [section], [{**section, "risk_id": "risk-1"}] * 2):
            with self.assertRaisesRegex(ValueError, "exactly once"):
                validate_presentation({"sections": sections}, [risk])

    def test_unknown_risk_type_is_rejected(self):
        detector = Detector()
        self.run_live(detector, Reporter())
        raw = detector.detect(detector.payload)
        raw["risks"][0]["risk_type"] = "unknown-type"
        validated = validate_detection(raw, detector.payload)
        self.assertEqual(validated["risks"], [])
        self.assertEqual(len(validated["rejected"]), 1)

    def test_targets_and_distinct_citations_are_enforced(self):
        detector = Detector()
        self.run_live(detector, Reporter())
        raw = detector.detect(detector.payload)
        raw["risks"][0]["target_item_ids"] = ["not-in-plan"]
        raw["risks"][0]["citations"] *= 2
        raw["risks"][0]["citations"] = [raw["risks"][0]["citations"][0]] * 2
        self.assertEqual(validate_detection(raw, detector.payload)["risks"], [])

    def test_duplicate_risk_ids_are_rejected(self):
        detector = Detector()
        self.run_live(detector, Reporter())
        raw = detector.detect(detector.payload)
        raw["risks"] *= 2
        with self.assertRaises(ValueError):
            Detection.model_validate(raw)


class AdapterTests(unittest.TestCase):
    def test_remote_endpoint_and_credential_urls_are_rejected(self):
        for endpoint in ("https://example.com/v1", "http://user:pass@localhost/v1",
                         "http://localhost/v1?secret=value", "file:///v1", "http://localhost/other"):
            with self.assertRaisesRegex(ValueError, "loopback"):
                LocalSLM(endpoint, "model")

    def test_local_adapter_sends_schema_and_validates_response_model(self):
        result = {"model": "trained", "choices": [{"finish_reason": "stop",
                  "message": {"content": json.dumps({"risks": [], "limitations": []})}}]}
        class Response:
            def __enter__(self):
                return self
            def __exit__(self, *args):
                return False
            def read(self, limit):
                return json.dumps(result).encode()
        class Opener:
            def open(self, request, timeout):
                body = json.loads(request.data)
                self_body.append(body)
                return Response()
        self_body = []
        with patch("nabu.risk.models.build_opener", return_value=Opener()):
            detector = LocalSLM("http://127.0.0.1:8080/v1", "trained")
            self.assertEqual(detector.detect({"plan": {}})["risks"], [])
            self.assertEqual(self_body[0]["response_format"]["type"], "json_schema")
            result["model"] = "wrong"
            with self.assertRaisesRegex(ValueError, "different model"):
                detector.detect({})
            result["model"] = "trained"
            result["choices"][0]["finish_reason"] = "length"
            with self.assertRaisesRegex(ValueError, "finish normally"):
                detector.detect({})
