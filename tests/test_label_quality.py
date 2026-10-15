import json
from pathlib import Path
import tempfile
import unittest

from nabu.labelling import encode
from nabu.risk.classifier import RUBRICS, TARGET_DEFINITION
from nabu.risk.label_quality import combine_labels, evaluate_labels, make_reference, split_data, write_bundle, read_rows


class QualityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def example(self, eid, item_id, cutoff, title=None, group=None):
        return {"example_id": eid, "group_item_ids": group or [item_id],
                "input": {"as_of": cutoff, "ticket": {"id": item_id, "source_key": item_id,
                          "fields": {"title": title or f"Unique ticket content {item_id}", "description": None},
                          "unknown_fields": ["description"]}, "context": {"plans": []}}}

    def dataset(self, name, rows, horizon):
        output = self.root / name
        labels = [{"example_id": row["example_id"], "state": "no_observed_signal",
                   "observation_window": {"through": horizon},
                   "targets": {"estimation": None, "rework": 1, "dependency": None}} for row in rows]
        write_bundle(output, {"inputs.jsonl": rows, "labels.jsonl": labels}, {"dataset_sha256": name})
        return output

    def predictions(self, name, dataset, rows, targets, model="teacher-a"):
        source = json.loads((dataset / "manifest.json").read_text())
        predictions = []
        for row, target in zip(rows, targets):
            predictions.append({"example_id": row["example_id"], "model": model, "served_model": model,
                                "classification": {risk: {"target": target, "choice": "risk" if target == 1 else "no_risk" if target == 0 else "insufficient_evidence",
                                    "confidence": 0.9, "evidence_confidence": 0.9, "abstention_reasons": [], "evidence": []}
                                    for risk in RUBRICS}})
        result = write_bundle(self.root / name, {"predictions.jsonl": predictions},
                            {"target_definition": TARGET_DEFINITION, "model": model, "provider": "jev",
                             "inputs_sha256": source["files"]["inputs.jsonl"]})
        manifest = {**result, "predictions_sha256": result["files"]["predictions.jsonl"]}
        (self.root / name / "manifest.json").write_text(json.dumps(manifest))
        return self.root / name

    def test_consensus_vetoes_disagreement_and_never_uses_outcomes_as_votes(self):
        rows = [self.example("a", "ticket-a", "2021-01-01"), self.example("b", "ticket-b", "2021-01-01")]
        dataset = self.dataset("dataset", rows, "2021-02-01")
        first = self.predictions("first", dataset, rows, [0, 1])
        second = self.predictions("second", dataset, rows, [0, 0], "teacher-b")
        result = combine_labels(dataset, [first, second], self.root / "consensus")
        self.assertEqual(result["training_examples"], 1)
        labels = read_rows(self.root / "consensus" / "labels.jsonl")
        self.assertEqual(labels[0]["targets"]["rework"], 0)
        self.assertEqual(labels[0]["decisions"]["rework"]["later_outcome_proxy"], 1)
        self.assertIsNone(labels[1]["targets"]["rework"])
        self.assertEqual(labels[1]["decisions"]["rework"]["reason"], "disagreement")
        with self.assertRaisesRegex(ValueError, "same model"):
            combine_labels(dataset, [first, first], self.root / "bad")

    def test_review_sample_is_blinded_and_unreviewed_sample_cannot_score(self):
        rows = [self.example(str(i), f"ticket-{i}", "2021-01-01") for i in range(5)]
        dataset = self.dataset("dataset", rows, "2021-02-01")
        predictions = self.predictions("teacher", dataset, rows, [1, 0, None, 1, None])
        make_reference(dataset, predictions, self.root / "reference", size=4)
        sample = read_rows(self.root / "reference" / "reference.jsonl")
        self.assertEqual(len({r["example_id"] for r in sample}), 4)
        self.assertTrue(all(not r["reviewed"] and all(v is None for v in r["targets"].values()) for r in sample))
        self.assertNotIn("confidence", encode(sample))
        with self.assertRaisesRegex(ValueError, "No independently reviewed"):
            evaluate_labels(dataset, predictions, self.root / "reference" / "reference.jsonl", self.root / "eval")

    def test_metrics_count_abstained_positives_as_missed(self):
        rows = [self.example(str(i), f"ticket-{i}", "2021-01-01") for i in range(4)]
        dataset = self.dataset("dataset", rows, "2021-02-01")
        predictions = self.predictions("teacher", dataset, rows, [1, 1, None, 0])
        reference = self.root / "gold.jsonl"
        reference.write_text("".join(encode({"example_id": row["example_id"], "target_definition": TARGET_DEFINITION,
                                             "reviewed": True, "reviewer": "independent-reviewer",
                                             "targets": {r: truth for r in RUBRICS}}) + "\n"
                                     for row, truth in zip(rows, [1, 0, 1, 0])))
        report = evaluate_labels(dataset, predictions, reference, self.root / "evaluation")
        for metric in report["metrics"].values():
            self.assertEqual(metric["precision"], 0.5)
            self.assertEqual(metric["recall_including_abstentions"], 0.5)
            self.assertEqual(metric["coverage"], 0.75)
            self.assertIsNone(metric["threshold_sweep"][-1]["precision"])

    def test_time_splits_group_repeat_epic_and_duplicate_without_leakage(self):
        early = [self.example("early-a", "same-ticket", "2020-01-01T00:00:00.000000Z"),
                 self.example("early-b", "only-train", "2020-01-01T00:00:00.000000Z"),
                 self.example("early-c", "duplicate-1", "2020-01-01T00:00:00.000000Z", title="Identical long title to prevent duplicate leakage"),
                 self.example("early-d", "epic-child", "2020-01-01T00:00:00.000000Z", group=["epic-child", "parent"])]
        later = [self.example("later-a", "same-ticket", "2022-01-01T00:00:00.000000Z"),
                 self.example("later-c", "duplicate-2", "2022-01-01T00:00:00.000000Z", title="Identical long title to prevent duplicate leakage"),
                 self.example("later-d", "parent", "2022-01-01T00:00:00.000000Z")]
        validation = [self.example("val", "only-validation", "2021-01-01T00:00:00.000000Z")]
        crossing = [self.example("cross", "crossing", "2020-12-01T00:00:00.000000Z")]
        sources = [self.dataset("early", early, "2020-04-01T00:00:00.000000Z"),
                   self.dataset("later", later, "2022-04-01T00:00:00.000000Z"),
                   self.dataset("val", validation, "2021-04-01T00:00:00.000000Z"),
                   self.dataset("cross", crossing, "2021-04-01T00:00:00.000000Z")]
        result = split_data(sources, self.root / "splits", "2020-12-31", "2021-12-31")
        self.assertEqual(result["counts"], {"train": 1, "test": 3, "validation": 1, "quarantine": 4})
        groups = {}
        for row in read_rows(self.root / "splits" / "assignments.jsonl"):
            if row["split"] != "quarantine":
                self.assertEqual(groups.setdefault(row["group_id"], row["split"]), row["split"])


if __name__ == "__main__":
    unittest.main()
