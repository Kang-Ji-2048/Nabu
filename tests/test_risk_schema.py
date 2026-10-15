"""Versioned schema exports must preserve the already-trained detector contract."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from nabu.cli import main
from nabu.risk.contracts import Detection
from nabu.risk.schema import risk_schema


class RiskSchemaTests(unittest.TestCase):
    def test_default_cli_preserves_trained_v1_schema_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "detector.json"
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertIsNone(main(["slm-schema", "--output", str(destination)]))
            self.assertEqual(json.loads(destination.read_text()), Detection.model_json_schema())
            self.assertEqual(json.loads(output.getvalue())["version"], "nabu-assess-v1")
            original = destination.read_bytes()
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                main(["slm-schema", "--output", str(destination)])
            self.assertEqual(error.exception.code, 1)
            self.assertEqual(destination.read_bytes(), original)

    def test_checked_in_workflow_schema_matches_export_and_resolves_all_local_refs(self):
        schema, version = risk_schema("workflow")
        self.assertEqual(version, "nabu-risk-workflow-v2")
        artifact = Path(__file__).resolve().parents[1] / "docs/schemas/risk-workflow-v2.schema.json"
        self.assertEqual(json.loads(artifact.read_text()), schema)
        self.assertEqual(len(schema["oneOf"]), 6)

        def check_references(node):
            if isinstance(node, dict):
                if "$ref" in node:
                    self.assertTrue(node["$ref"].startswith("#/$defs/"))
                    self.assertIn(node["$ref"].removeprefix("#/$defs/"), schema["$defs"])
                for value in node.values():
                    check_references(value)
            elif isinstance(node, list):
                for value in node:
                    check_references(value)

        check_references(schema)

    def test_cli_selects_versioned_presentation_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "presentation.json"
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertIsNone(main(["slm-schema", "--contract", "presentation", "--output", str(destination)]))
            schema = json.loads(destination.read_text())
            self.assertEqual(schema["properties"]["schema_version"]["const"], "nabu-presentation-v2")
            self.assertEqual(json.loads(output.getvalue())["version"], "nabu-presentation-v2")

    def test_unknown_contract_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown risk contract"):
            risk_schema("invented")


if __name__ == "__main__":
    unittest.main()
