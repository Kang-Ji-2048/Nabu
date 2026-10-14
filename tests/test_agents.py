import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from langchain_core.messages import AIMessage, ToolMessage

from nabu.agents.contracts import CriticVerdict, SearchArgs
from nabu.agents.evidence import execute_tool, freeze_evidence
from nabu.agents.runner import run_review
from nabu.pipeline import load


CUTOFF = "2014-01-05T12:00:00Z"


class ScriptedModel:
    """Deterministic model substitute to test workflow contracts, not AI quality."""
    def __init__(self, steps, decisions=()):
        self.steps = iter(steps)
        self.decisions = iter(decisions)
        self.calls = 0
        self.critic_calls = 0

    def bind_tools(self, tools):
        return self

    def with_structured_output(self, schema):
        owner = self
        class Critic:
            def invoke(self, messages):
                owner.critic_calls += 1
                return CriticVerdict.model_validate({"decisions": next(owner.decisions)})
        return Critic()

    def invoke(self, messages):
        self.calls += 1
        step = next(self.steps)
        if isinstance(step, Exception):
            raise step
        if isinstance(step, str):
            return AIMessage(content=step)
        name, args = step
        return AIMessage(content="", tool_calls=[{"name": name, "args": args, "id": f"test-{self.calls}"}])


class AgentTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.database = self.root / "source.sqlite"
        rows = [{"table": "Project", "row": {"ID": 1, "Project_Key": "TEST"}}]
        issues = [
            (1, "TEST-1", "FUTURE_SECRET_ROOT", "FUTURE_SECRET_DESCRIPTION", "2014-01-01", "2014-01-20", "Done"),
            (2, "TEST-2", "Build module", "Build the artifact.", "2014-01-02", "2014-01-03", "To Do"),
            (3, "TEST-3", "Packaging compatibility tests", "Test custom modules against deployment layout.", "2013-01-01", "2013-12-01", "Done"),
            (4, "TEST-4", "Module packaging verification", "Check compatibility before shipping modules.", "2013-01-01", "2013-12-01", "Done"),
            (5, "TEST-5", "FUTURE_SECRET_MODULE", "FUTURE_SECRET_PACKAGING", "2014-01-10", "2014-01-20", "Done"),
        ]
        for iid, key, title, description, created, updated, status in issues:
            rows.append({"table": "Issue", "row": {"ID": iid, "Project_ID": 1, "Issue_Key": key,
                "Title": title, "Description": description, "Type": "Task", "Story_Point": 3,
                "Creation_Date": created, "Last_Updated": updated, "Status": status}})
        for eid, field, before, after in [(100, "summary", "Deploy custom modules", "FUTURE_SECRET_ROOT"),
                                          (101, "description", "Ship custom modules.", "FUTURE_SECRET_DESCRIPTION")]:
            rows.append({"table": "Change_Log", "row": {"ID": eid, "Issue_ID": 1, "Field": field,
                "Creation_Date": "2014-01-20", "From_String": before, "To_String": after}})
        rows.append({"table": "Change_Log", "row": {"ID": 102, "Issue_ID": 1, "Field": "Epic Child",
            "Creation_Date": "2014-01-03", "To_String": "TEST-2"}})
        path = self.root / "source.jsonl"
        path.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
        self.assertEqual(load(path, self.database)["rejected"], 0)

    def finding(self, *, bad_id=False, bad_quote=False):
        return {"id": "gap-1", "claim": "Compatibility testing is not visible in observed scope.",
                "rationale": "Two prior module packaging tasks explicitly included compatibility checks.",
                "suggested_action": "Confirm whether compatibility tests are covered before adding a ticket.",
                "target_item_ids": ["tawos-v1.1:1"], "severity": "medium",
                "scope_basis": "not_visible_in_observed_scope",
                "citations": [
                    {"item_id": "tawos-v1.1:999" if bad_id else "tawos-v1.1:3", "field": "title",
                     "quote": "Invented quote" if bad_quote else "Packaging compatibility tests"},
                    {"item_id": "tawos-v1.1:4", "field": "description", "quote": "Check compatibility before shipping modules."},
                ]}

    def steps(self, finding):
        return [("search_prior_work", {"query": "module packaging", "limit": 5}),
                ("submit_findings", {"findings": [finding], "limitations": ["Observed scope is incomplete."]})]

    def run_model(self, model, **options):
        return run_review(self.database, "TEST-1", CUTOFF, self.root / "run",
                          model=model, model_id="test-only-model", **options)

    def test_search_and_item_tools_never_expose_future_records_or_text(self):
        state = {**freeze_evidence(self.database, "TEST-1", CUTOFF), "evidence": {}}
        result, evidence = execute_tool("search_prior_work", SearchArgs(query="module packaging"), state)
        self.assertEqual({item["source_key"] for item in result["items"]}, {"TEST-3", "TEST-4"})
        self.assertNotIn("FUTURE_SECRET", json.dumps(result))
        self.assertNotIn("tawos-v1.1:5", state["corpus"])
        self.assertNotIn("tawos-v1.1:1", evidence)

    def test_valid_citations_must_pass_critic_before_publication(self):
        model = ScriptedModel(self.steps(self.finding()), [[{"finding_id": "gap-1", "action": "accept", "reason": "Comparable work and specific evidence; warning is conditional."}]])
        report = self.run_model(model)
        self.assertEqual(len(report["findings"]), 1)
        self.assertEqual(model.critic_calls, 1)
        self.assertEqual(report["usage"], {"model_calls": 3, "tool_calls": 2, "rounds": 1})

    def test_semantic_retrieval_preserves_citation_and_historical_boundaries(self):
        from test_semantic import FakeEncoder
        model = ScriptedModel(self.steps(self.finding()), [[{"finding_id": "gap-1", "action": "accept", "reason": "Supported by comparable prior work."}]])
        report = self.run_model(model, retrieval="semantic", encoder=FakeEncoder(), embedding_cache=self.root / "vectors.sqlite")
        self.assertEqual(len(report["findings"]), 1)
        self.assertEqual(report["retrieval"]["method"], "semantic_cosine")
        self.assertEqual(report["retrieval"]["proposed_categories"], 0)
        self.assertNotIn("FUTURE_SECRET", json.dumps(report))

    def test_semantic_resume_reuses_vectors_and_frozen_source(self):
        from test_semantic import FakeEncoder
        encoder = FakeEncoder()
        paused = self.run_model(ScriptedModel([]), retrieval="semantic", encoder=encoder,
                                embedding_cache=self.root / "vectors.sqlite", pause_after_prepare=True)
        self.assertGreater(encoder.encoded_documents, 0)
        connection = sqlite3.connect(self.database)
        connection.execute("UPDATE work_item SET title='CHANGED_SOURCE',description='CHANGED_SOURCE'")
        connection.commit()
        connection.close()
        resumed_encoder = FakeEncoder()
        model = ScriptedModel(self.steps(self.finding()), [[{"finding_id": "gap-1", "action": "accept", "reason": "Supported by frozen evidence."}]])
        report = run_review(None, None, None, self.root / "run", resume=True, model=model, encoder=resumed_encoder)
        self.assertEqual(report["evidence_fingerprint"], paused["evidence_fingerprint"])
        self.assertEqual(resumed_encoder.encoded_documents, 0)
        self.assertEqual(len(report["findings"]), 1)
        with self.assertRaisesRegex(ValueError, "retrieval or embedding model"):
            run_review(None, None, None, self.root / "run", resume=True, retrieval="lexical")

    def test_semantic_review_without_prior_text_can_finish_without_a_model_download(self):
        connection = sqlite3.connect(self.database)
        connection.execute("UPDATE work_item SET created_at='2099-01-01T00:00:00.000000Z' WHERE source_key IN ('TEST-3','TEST-4')")
        connection.commit()
        connection.close()
        report = self.run_model(ScriptedModel([("submit_findings", {"findings": [], "limitations": ["No eligible prior text."]})]),
                                retrieval="semantic", embedding_model_dir=self.root / "absent-model")
        self.assertEqual(report["status"], "completed")
        self.assertEqual(report["retrieval"]["method"], "semantic_unavailable")

    def test_invented_citation_is_withheld_and_revised(self):
        steps = self.steps(self.finding(bad_id=True)) + [("submit_findings", {"findings": [], "limitations": ["No supported finding."]})]
        model = ScriptedModel(steps)
        report = self.run_model(model)
        self.assertEqual(report["findings"], [])
        self.assertEqual(report["usage"]["rounds"], 2)
        self.assertEqual(model.critic_calls, 0)
        events = json.loads((self.root / "run" / "events.json").read_text())
        self.assertTrue(any(event["stage"] == "validate" and event["rejected"] == 1 for event in events))

    def test_exact_quote_validation_blocks_fabrication(self):
        report = self.run_model(ScriptedModel(self.steps(self.finding(bad_quote=True))), max_rounds=1)
        self.assertEqual(report["findings"], [])
        self.assertTrue(any("citation validation" in note for note in report["limitations"]))

    def test_critic_can_send_a_finding_back_once(self):
        decisions = [
            [{"finding_id": "gap-1", "action": "revise", "reason": "Look for counterexamples before concluding."}],
            [{"finding_id": "gap-1", "action": "accept", "reason": "Revised conditional finding is adequately supported."}],
        ]
        model = ScriptedModel(self.steps(self.finding()) + [("search_prior_work", {"query": "compatibility", "completed_only": False}),
                               ("submit_findings", {"findings": [self.finding()], "limitations": []})], decisions)
        report = self.run_model(model)
        self.assertEqual(report["usage"]["rounds"], 2)
        self.assertEqual(model.critic_calls, 2)
        self.assertEqual(len(report["findings"]), 1)

    def test_model_cannot_change_cutoff_or_call_arbitrary_tools(self):
        steps = [("search_prior_work", {"query": "module", "as_of": "2099-01-01"}),
                 ("execute_sql", {"query": "SELECT * FROM work_item"}),
                 ("submit_findings", {"findings": [], "limitations": []})]
        report = self.run_model(ScriptedModel(steps))
        self.assertEqual(report["findings"], [])
        errors = [event for event in json.loads((self.root / "run" / "events.json").read_text()) if event.get("status") == "error"]
        self.assertEqual(len(errors), 2)

    def test_budget_exhaustion_never_accepts_unreviewed_findings(self):
        model = ScriptedModel(self.steps(self.finding()))
        report = self.run_model(model, max_model_calls=2)
        self.assertEqual(report["findings"], [])
        self.assertEqual(report["status"], "incomplete_budget")
        self.assertEqual(model.critic_calls, 0)

    def test_unstructured_model_response_cannot_bypass_budget_or_contract(self):
        report = self.run_model(ScriptedModel(["Trust me, this is high risk"]), max_model_calls=1)
        self.assertEqual(report["findings"], [])
        self.assertEqual(report["status"], "incomplete_budget")

    def test_tool_budget_stops_investigation_without_publishing(self):
        report = self.run_model(ScriptedModel(self.steps(self.finding())), max_tool_calls=1)
        self.assertEqual(report["findings"], [])
        self.assertEqual(report["status"], "incomplete_budget")
        self.assertEqual(report["usage"]["tool_calls"], 1)

    def test_critic_drop_is_not_treated_as_a_validated_warning(self):
        model = ScriptedModel(self.steps(self.finding()), [[{"finding_id": "gap-1", "action": "drop", "reason": "The examples do not establish a relevant gap."}]])
        report = self.run_model(model)
        self.assertEqual(report["findings"], [])
        self.assertEqual(report["status"], "completed")

    def test_resume_uses_frozen_evidence_after_source_database_changes(self):
        run_dir = self.root / "run"
        paused = self.run_model(ScriptedModel([]), pause_after_prepare=True)
        self.assertEqual(paused["status"], "paused")
        connection = sqlite3.connect(self.database)
        connection.execute("UPDATE work_item SET title='CHANGED_SOURCE',description='CHANGED_SOURCE'")
        connection.commit()
        connection.close()
        model = ScriptedModel(self.steps(self.finding()), [[{"finding_id": "gap-1", "action": "accept", "reason": "Valid against the frozen evidence."}]])
        resumed = run_review(None, None, None, run_dir, resume=True, model=model)
        self.assertEqual(resumed["evidence_fingerprint"], paused["evidence_fingerprint"])
        self.assertEqual(len(resumed["findings"]), 1)
        self.assertEqual([event["stage"] for event in json.loads((run_dir / "events.json").read_text())].count("prepare"), 1)
        with self.assertRaisesRegex(ValueError, "epic or cutoff"):
            run_review(None, "TEST-1", "2099-01-01", run_dir, resume=True, model=model)

    def test_failed_model_node_can_resume_without_repeating_preparation(self):
        run_dir = self.root / "run"
        with self.assertRaisesRegex(RuntimeError, "simulated failure"):
            self.run_model(ScriptedModel([RuntimeError("simulated failure")]))
        self.assertEqual(json.loads((run_dir / "review.json").read_text())["status"], "failed")
        model = ScriptedModel(self.steps(self.finding()), [[{"finding_id": "gap-1", "action": "accept", "reason": "Supported finding."}]])
        report = run_review(None, None, None, run_dir, resume=True, model=model)
        self.assertEqual(len(report["findings"]), 1)
        events = json.loads((run_dir / "events.json").read_text())
        self.assertEqual([event["stage"] for event in events].count("prepare"), 1)

    def test_anthropic_adapter_can_bind_domain_tool_schemas_without_network(self):
        from langchain_anthropic import ChatAnthropic
        from nabu.agents.contracts import tool_specs
        adapter = ChatAnthropic(model="test-model", api_key="test-not-a-real-key")
        bound = adapter.bind_tools(tool_specs())
        self.assertEqual({tool["name"] for tool in bound.kwargs["tools"]}, {tool["name"] for tool in tool_specs()})
