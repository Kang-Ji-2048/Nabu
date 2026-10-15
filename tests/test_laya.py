import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from nabu.labelling import encode
from nabu.risk.classifier import RUBRICS, validate_result
from nabu.risk.label_evidence import classifier_payload
from nabu.risk.laya import LayaClassifier, MANIFEST, RUNTIME, verify_model


class Agent:
    def __init__(self, truncated=False, collapsed=False):
        self.truncated = truncated
        self.collapsed = collapsed
        self.batches = []

    def predict(self, state, questions, **options):
        self.state = state
        usage = {"truncated": self.truncated}
        if self.collapsed:
            usage["options"] = {"scope_gap": {"collapsed": True}}
        return {"usage": usage, "answers": {risk: {"choice": "risk", "confidence": 0.2,
                "answer_confidence": 0.92, "probabilities": {"risk": 0.92, "no_risk": 0.04, "insufficient_evidence": 0.04}}
                for risk in questions}}

    def predict_batch(self, states, questions, **options):
        self.batches.extend(states)
        return [{"usage": {"truncated": False}, "answers": {"support": {"choice": "supports", "answer_confidence": 0.94}}}
                for state in states]


class LayaTests(unittest.TestCase):
    def payload(self):
        return classifier_payload({"input": {"as_of": "2021-01-01", "ticket": {
            "id": "XD-1", "source_key": "XD-1", "fields": {"title": "Deployment blocked by missing API contract.",
            "description": None, "acceptance_criteria": None}, "unknown_fields": ["description", "acceptance_criteria"]}}})

    def manifest(self):
        return {"repository": "test-laya", "revision": "pinned", "max_length": 1024}

    def test_uses_answer_confidence_and_exact_local_evidence(self):
        agent = Agent()
        teacher = LayaClassifier("unused", agent=agent, manifest=self.manifest())
        payload = self.payload()
        result = validate_result(teacher.classify(payload), 0.8, payload)
        self.assertTrue(all(r["target"] == 1 for r in result.values()))
        self.assertEqual(result["dependency"]["confidence"], 0.92)
        self.assertEqual(result["dependency"]["entropy_confidence"], 0.2)
        self.assertNotIn("snippets", agent.state)
        self.assertTrue(agent.batches)
        self.assertEqual(teacher.served_model, "test-laya@pinned")

    def test_truncation_or_option_collapse_never_enters_training(self):
        for agent in (Agent(truncated=True), Agent(collapsed=True)):
            teacher = LayaClassifier("unused", agent=agent, manifest=self.manifest())
            payload = self.payload()
            result = validate_result(teacher.classify(payload), 0.8, payload)
            self.assertTrue(all(r["target"] is None for r in result.values()))
            self.assertEqual(agent.batches, [])
            self.assertIn("abstention_reason", teacher.last_coverage)

    def test_modified_local_weights_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "model.safetensors").write_bytes(b"original")
            files = {"model.safetensors": hashlib.sha256(b"original").hexdigest()}
            manifest = {"version": "nabu.laya-artifact.v1", "runtime": RUNTIME, "files": files,
                        "artifact_sha256": hashlib.sha256(encode(files).encode()).hexdigest()}
            (root / MANIFEST).write_text(json.dumps(manifest))
            verify_model(root)
            (root / "model.safetensors").write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                verify_model(root)


if __name__ == "__main__":
    unittest.main()
