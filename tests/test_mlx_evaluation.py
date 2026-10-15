import importlib.util
import json
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('mlx_evaluation', Path(__file__).resolve().parents[1]/'scripts/evaluate-slm-mlx.py')
evaluation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaluation)


class EvaluationTests(unittest.TestCase):
    def test_incomplete_output_is_not_a_negative_prediction(self):
        result = evaluation.assess('{"risks":[],"limitations":[]}', 'length', {})
        self.assertFalse(result['schema_valid'])
        refs = [{'id': 'positive', 'target': {'risks': [{}]}}]
        metrics = evaluation.summarize([{'id': 'positive', **result}], refs)
        self.assertEqual(metrics['scorable_ai_positive_cases'], 0)
        self.assertEqual(metrics['ai_positive_reference_cases'], 1)

    def test_invalid_citations_do_not_count_as_valid_findings(self):
        rows = [json.loads(line) for line in (Path(__file__).resolve().parents[1]/'data/external-test/mesos-ai-reference-v1/reference-labels.jsonl').read_text().splitlines() if line.strip()]
        row = next(r for r in rows if r['target']['risks'])
        target = json.loads(json.dumps(row['target']))
        for risk in target['risks']:
            for citation in risk['citations']:
                citation['quote'] = 'A fabricated quote that is absent from the supplied historical evidence.'
        result = evaluation.assess(json.dumps(target), 'stop', row['input'])
        self.assertTrue(result['schema_valid'])
        self.assertGreater(result['proposed_findings'], 0)
        self.assertEqual(result['valid_findings'], 0)
        self.assertTrue(result['citation_errors'])


if __name__ == '__main__':
    unittest.main()
