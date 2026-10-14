"""CPU-only candidate packaging tests using synthetic historical evidence."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("slm_candidates", Path(__file__).resolve().parents[1] / "scripts" / "validate-slm-candidates.py")
candidate_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(candidate_module)


def item(iid, title):
    return {"id": iid, "source_key": iid, "created_at": "2014-01-01T00:00:00Z",
            "fields": {"title": title, "description": "Known historical description."},
            "unknown_fields": [], "truncated_fields": []}


def source_row(split, iid):
    return {"id": iid, "split": split, "epic": iid, "group": iid,
            "as_of": "2014-02-01T00:00:00Z", "evidence_fingerprint": "f" * 64,
            "review_status": "draft", "custom_metadata": {"preserve": True},
            "input": {"plan": {"root": item(iid, "Module compatibility verification"),
                               "members": [], "as_of": "2014-02-01T00:00:00Z"},
                      "prior_work": [item("PRIOR-1", "Module incompatibility causes failure"),
                                     item("PRIOR-2", "Package incompatibility causes failure")],
                      "allowed_risk_types": ["compatibility"], "coverage": {"warning": "Limited evidence."}}}


def proposed_target():
    return {"risks": [{"id": "risk-1", "risk_type": "compatibility", "claim": "Compatibility requires verification.",
                       "rationale": "Historical failures identify the compatibility concern.",
                       "suggested_action": "Confirm compatibility tests.", "severity": "medium",
                       "target_item_ids": ["TRAIN-1"],
                       "citations": [{"item_id": "PRIOR-1", "field": "title", "quote": "Module incompatibility causes failure"},
                                     {"item_id": "PRIOR-2", "field": "title", "quote": "Package incompatibility causes failure"}]}],
            "limitations": ["Historical ticket text does not prove a future failure."]}


class CandidatePackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.train = self.root / "train-drafts.jsonl"
        self.validation = self.root / "validation-drafts.jsonl"
        self.proposals = self.root / "proposals.jsonl"
        self.output = self.root / "output"
        self.train_row = source_row("train", "TRAIN-1")
        self.validation_row = source_row("validation", "VALIDATION-1")
        self.write(self.train, [self.train_row])
        self.write(self.validation, [self.validation_row])

    def write(self, path, rows):
        path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")

    def run_package(self, target=None, proposals=None):
        if proposals is None:
            proposals = [{"id": "TRAIN-1", "target": target or proposed_target()},
                         {"id": "VALIDATION-1", "target": {"risks": [], "limitations": ["No supported risk in supplied text."]}}]
        self.write(self.proposals, proposals)
        return candidate_module.package_candidates(self.train, self.validation, self.proposals, self.output)

    def read(self, filename):
        return [json.loads(line) for line in (self.output / filename).read_text().splitlines()]

    def test_valid_preserves_source_fields_and_never_claims_human_review(self):
        summary = self.run_package()
        rows = self.read("generated-labels.jsonl")
        for before, after in zip([self.train_row, self.validation_row], rows):
            for key, value in before.items():
                if key != "review_status":
                    self.assertEqual(after[key], value)
            self.assertEqual(after["review_status"], "generated_unreviewed")
            self.assertFalse(after["label_source"]["human_approved"])
            self.assertEqual(after["label_source"]["generator"], "Codex")
            self.assertNotIn("reviewer", after)
            self.assertNotIn("reviewer", after["label_source"])
            self.assertEqual(after["source_input_sha256"], candidate_module.identity_sha256(before["input"]))
        self.assertEqual(summary["totals"]["risk_examples"], 1)
        self.assertEqual(summary["totals"]["no_risk_examples"], 1)
        review = (self.output / "review.md").read_text()
        self.assertIn("PRIOR-1", review)
        self.assertIn("Module incompatibility causes failure", review)

    def test_rejected_citation_is_failed_not_rewritten_as_no_risk(self):
        target = proposed_target()
        target["risks"][0]["citations"][0]["quote"] = "Invented quote"
        summary = self.run_package(target=target)
        self.assertEqual(summary["totals"]["failed_examples"], 1)
        self.assertEqual(summary["totals"]["no_risk_examples"], 1)
        self.assertEqual([row["id"] for row in self.read("generated-labels.jsonl")], ["VALIDATION-1"])
        failure = next(row for row in self.read("label-events.jsonl") if row["id"] == "TRAIN-1")
        self.assertEqual(failure["target"], target)
        self.assertEqual(failure["status"], "failed")
        self.assertTrue(failure["errors"])

    def test_missing_proposal_recorded_without_empty_label(self):
        summary = self.run_package(proposals=[{"id": "TRAIN-1", "target": proposed_target()}])
        self.assertEqual(summary["totals"]["missing_examples"], 1)
        self.assertEqual(summary["totals"]["no_risk_examples"], 0)
        self.assertEqual(len(self.read("generated-labels.jsonl")), 1)
        self.assertIn("missing_proposal", (self.output / "label-events.jsonl").read_text())

    def test_malformed_detection_is_logged_and_review_remains_readable(self):
        target = proposed_target()
        target["risks"][0]["citations"] = None
        summary = self.run_package(proposals=[{"id": "TRAIN-1", "target": target,
                                              "labelling_questions": "invalid questions"}])
        self.assertEqual(summary["totals"]["failed_examples"], 1)
        self.assertEqual(self.read("generated-labels.jsonl"), [])
        self.assertIn("Validation failures", (self.output / "review.md").read_text())
        failure = next(row for row in self.read("label-events.jsonl") if row["id"] == "TRAIN-1")
        self.assertEqual(failure["target"], target)

    def test_unhashable_citation_id_is_logged_with_complete_audit_outputs(self):
        target = proposed_target()
        target["risks"][0]["citations"][0]["item_id"] = ["PRIOR-1"]
        summary = self.run_package(target=target)
        self.assertEqual(summary["totals"]["failed_examples"], 1)
        self.assertEqual({path.name for path in self.output.iterdir()},
                         {"generated-labels.jsonl", "label-events.jsonl", "review.md", "summary.json"})
        self.assertEqual([row["id"] for row in self.read("generated-labels.jsonl")], ["VALIDATION-1"])
        failure = next(row for row in self.read("label-events.jsonl") if row["id"] == "TRAIN-1")
        self.assertEqual(failure["target"], target)
        self.assertIn("UNKNOWN TICKET", (self.output / "review.md").read_text())

    def test_review_render_failure_does_not_publish_partial_outputs(self):
        with patch.object(candidate_module, "review_document", side_effect=RuntimeError("Render failed")):
            with self.assertRaisesRegex(RuntimeError, "Render failed"):
                self.run_package()
        self.assertFalse(self.output.exists())

    def test_staged_write_failure_does_not_publish_and_cleans_staging(self):
        original = Path.write_text

        def fail_events(path, *args, **kwargs):
            if path.name == "label-events.jsonl":
                raise OSError("Event write failed")
            return original(path, *args, **kwargs)

        with patch.object(Path, "write_text", fail_events):
            with self.assertRaisesRegex(OSError, "Event write failed"):
                self.run_package()
        self.assertFalse(self.output.exists())
        self.assertFalse(list(self.root.glob(".output-staging-*")))

    def test_test_split_rows_rejected(self):
        self.write(self.train, [source_row("test", "HELD-OUT")])
        self.write(self.proposals, [])
        with self.assertRaisesRegex(ValueError, "held-out test rows are forbidden"):
            candidate_module.package_candidates(self.train, self.validation, self.proposals, self.output)
        self.assertFalse(self.output.exists())

    def test_test_named_source_is_rejected_before_reading(self):
        self.write(self.proposals, [])
        with self.assertRaisesRegex(ValueError, "Held-out test source files are forbidden"):
            candidate_module.package_candidates(self.root / "test-drafts.jsonl", self.validation, self.proposals, self.output)

    def test_duplicate_proposals_all_fail_and_nonempty_output_refused(self):
        proposal = {"id": "TRAIN-1", "target": proposed_target()}
        summary = self.run_package(proposals=[proposal, deepcopy(proposal)])
        self.assertEqual(summary["totals"]["failed_examples"], 1)
        self.assertEqual(summary["totals"]["missing_examples"], 1)
        self.assertEqual(self.read("generated-labels.jsonl"), [])
        with self.assertRaisesRegex(ValueError, "must be empty"):
            candidate_module.package_candidates(self.train, self.validation, self.proposals, self.output)

    def test_unknown_and_malformed_proposals_are_logged(self):
        self.proposals.write_text('{bad json\n' + json.dumps({"id": "UNKNOWN", "target": {"risks": [], "limitations": []}}) + '\n')
        summary = candidate_module.package_candidates(self.train, self.validation, self.proposals, self.output)
        self.assertEqual(summary["proposal_input_errors"], 2)
        self.assertEqual(summary["totals"]["missing_examples"], 2)
        self.assertEqual(len(self.read("label-events.jsonl")), 4)


if __name__ == "__main__":
    unittest.main()
