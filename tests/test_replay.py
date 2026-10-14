import hashlib
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from nabu.pipeline import load
from nabu.replay import HistoricalReader, write_replay


CUTOFF = "2014-01-05T12:00:00Z"


class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.database = self.root / "test.sqlite"
        records = [{"table": "Project", "row": {"ID": 1, "Project_Key": "TEST"}}]
        for iid, created, kind, estimate in [(1, "2014-01-01", "Story", 9), (2, "2014-01-02", "Bug", 8), (3, "2014-01-10", "Task", 13), (4, "2014-01-02", "Task", 5)]:
            records.append({"table": "Issue", "row": {"ID": iid, "Jira_ID": 500+iid, "Project_ID": 1, "Issue_Key": f"TEST-{iid}", "Type": kind, "Title": "FUTURE_SECRET_TITLE", "Description": "FUTURE_SECRET_DESCRIPTION", "Status": "Done", "Story_Point": estimate, "Creation_Date": created, "Resolution_Date": "2014-01-20", "Last_Updated": "2014-01-20"}})
        self.event_id = 100

        def event(iid, field, at, before, after, category="OTHER", from_id=None, to_id=None):
            self.event_id += 1
            records.append({"table": "Change_Log", "row": {"ID": self.event_id, "Issue_ID": iid, "Field": field, "Creation_Date": at, "From_String": before, "To_String": after, "Change_Type": category, "From_Value": from_id, "To_Value": to_id}})

        for iid, estimate, historical_type in [(1, 3, "Epic"), (2, 2, "Task")]:
            event(iid, "summary", "2014-01-10", f"Original title {iid}", "FUTURE_SECRET_TITLE")
            event(iid, "description", "2014-01-10", f"Original description {iid}", "FUTURE_SECRET_DESCRIPTION")
            event(iid, "status", "2014-01-10", "To Do", "Done", "STATUS")
            event(iid, "Story Points", "2014-01-10", str(estimate), str(estimate+6), "STORY_POINT")
            event(iid, "issuetype", "2014-01-10", historical_type, "Story" if iid == 1 else "Bug")
        event(1, "Actual Story Points", "2014-01-04", "0", "999", "STORY_POINT")
        event(1, "Epic Child", "2014-01-02", None, "TEST-2", to_id="502")
        event(2, "Epic Link", "2014-01-02", None, "TEST-1", to_id="501")
        event(1, "Epic Child", "2014-01-12", None, "TEST-3", to_id="503")
        event(1, "Epic Child", "2014-01-02", None, "TEST-4", to_id="504")
        event(1, "Epic Child", "2014-01-04", "TEST-4", None, from_id="504")
        records.extend([
            {"table": "Comment", "row": {"ID": 1, "Issue_ID": 1, "Creation_Date": "2014-01-03", "Comment": "FUTURE_SECRET_EDITED_COMMENT"}},
            {"table": "Issue_Link", "row": {"ID": 1, "Issue_ID": 2, "Target_Issue_ID": 3, "Description": "blocks"}},
        ])
        self.source = self.root / "source.jsonl"
        self.source.write_text("\n".join(json.dumps(record) for record in records), encoding="utf-8")
        self.assertEqual(load(self.source, self.database)["rejected"], 0)

    def read(self, cutoff=CUTOFF):
        reader = HistoricalReader(self.database, "TEST-1", cutoff)
        try:
            plan, audit = reader.plan()
            return plan, audit, reader.reveal(plan)
        finally:
            reader.close()

    def mutate(self, sql, params=()):
        connection = sqlite3.connect(self.database)
        try:
            connection.execute(sql, params)
            connection.commit()
        finally:
            connection.close()

    def test_reconstructs_fields_and_membership_without_outcomes(self):
        plan, audit, reveal = self.read()
        self.assertEqual(plan["root"]["fields"], {"title": "Original title 1", "description": "Original description 1", "type": "Epic", "status": "To Do", "estimate": 3.0})
        self.assertEqual([item["source_key"] for item in plan["members"]], ["TEST-2"])
        self.assertNotIn("FUTURE_SECRET", json.dumps(plan))
        self.assertNotIn("resolved_at", json.dumps(plan))
        self.assertNotIn("999", json.dumps(plan))
        self.assertEqual(plan["dependencies"]["status"], "unknown")
        self.assertEqual(plan["comments"]["status"], "excluded")
        self.assertTrue(any(e["at"] > plan["as_of"] for field in audit["root_fields"].values() for e in field["evidence"]))
        self.assertTrue(reveal["evaluation_only"])
        self.assertEqual(reveal["root_outcome"]["resolved_at"], "2014-01-20T00:00:00.000000Z")

    def test_later_snapshot_and_future_event_changes_do_not_change_plan(self):
        before, _, _ = self.read()
        self.mutate("UPDATE work_item SET title='DIFFERENT_FUTURE_TITLE',description='DIFFERENT_FUTURE_DESCRIPTION',estimate=700,status='Closed',resolved_at='2014-03-01T00:00:00.000000Z',updated_at='2014-03-01T00:00:00.000000Z'")
        self.mutate("UPDATE event SET to_value='DIFFERENT_FUTURE_TITLE' WHERE field='summary'")
        self.mutate("INSERT INTO event VALUES ('future-membership','tawos-v1.1:1','2014-02-01T00:00:00.000000Z','membership_changed','Epic Child',NULL,'TEST-4',NULL,'504')")
        after, _, reveal = self.read()
        self.assertEqual(before, after)
        self.assertEqual(reveal["root_outcome"]["title"], "DIFFERENT_FUTURE_TITLE")

    def test_missing_history_is_unknown_instead_of_current_value(self):
        self.mutate("DELETE FROM event WHERE field='summary'")
        plan, audit, _ = self.read()
        self.assertIsNone(plan["root"]["fields"]["title"])
        self.assertIn("title", plan["root"]["unknown_fields"])
        self.assertEqual(audit["root_fields"]["title"]["reason"], "no_temporal_evidence")
        self.assertNotIn("FUTURE_SECRET", json.dumps(plan))

    def test_known_null_is_distinct_from_unknown(self):
        self.mutate("UPDATE event SET from_value=NULL,from_id=NULL WHERE item_id='tawos-v1.1:1' AND field='Story Points'")
        plan, _, _ = self.read()
        self.assertIsNone(plan["root"]["fields"]["estimate"])
        self.assertNotIn("estimate", plan["root"]["unknown_fields"])

    def test_missing_display_value_is_not_mistaken_for_known_null(self):
        self.mutate("UPDATE event SET from_value=NULL,from_id='3' WHERE item_id='tawos-v1.1:1' AND field='Story Points'")
        self.mutate("UPDATE event SET from_value=NULL,from_id='10000' WHERE item_id='tawos-v1.1:1' AND field='status'")
        plan, audit, _ = self.read()
        self.assertEqual(plan["root"]["fields"]["estimate"], 3.0)
        self.assertIn("status", plan["root"]["unknown_fields"])
        self.assertEqual(audit["root_fields"]["status"]["reason"], "missing_display_value")

    def test_snapshot_fallback_requires_update_by_cutoff(self):
        self.mutate("DELETE FROM event WHERE item_id='tawos-v1.1:1' AND field='summary'")
        self.mutate("UPDATE work_item SET title='Known by cutoff',updated_at='2014-01-04T00:00:00.000000Z' WHERE id='tawos-v1.1:1'")
        plan, audit, _ = self.read()
        self.assertEqual(plan["root"]["fields"]["title"], "Known by cutoff")
        self.assertNotIn("title", plan["root"]["unknown_fields"])
        self.assertEqual(audit["root_fields"]["title"]["reason"], "snapshot_updated_by_cutoff")

    def test_cutoff_is_inclusive_and_timezone_normalized(self):
        self.mutate("INSERT INTO event VALUES ('at-cutoff','tawos-v1.1:1','2014-01-05T12:00:00.000000Z','text_changed','summary','Before cutoff','At cutoff',NULL,NULL)")
        self.mutate("UPDATE event SET from_value='At cutoff' WHERE item_id='tawos-v1.1:1' AND field='summary' AND at>'2014-01-05T12:00:00.000000Z'")
        plan, _, _ = self.read("2014-01-05T13:00:00+01:00")
        self.assertEqual(plan["root"]["fields"]["title"], "At cutoff")
        self.assertEqual(plan["as_of"], "2014-01-05T12:00:00.000000Z")

    def test_conflicting_history_fails_closed(self):
        self.mutate("INSERT INTO event VALUES ('conflict','tawos-v1.1:1','2014-01-10T00:00:00.000000Z','text_changed','summary','Conflicting old title','Other new title',NULL,NULL)")
        plan, audit, _ = self.read()
        self.assertIn("title", plan["root"]["unknown_fields"])
        self.assertEqual(audit["root_fields"]["title"]["reason"], "conflicting_history")

    def test_future_created_child_is_excluded_even_with_invalid_old_membership(self):
        self.mutate("INSERT INTO event VALUES ('invalid-creation','tawos-v1.1:1','2014-01-03T00:00:00.000000Z','membership_changed','Epic Child',NULL,'TEST-3',NULL,'503')")
        plan, audit, _ = self.read()
        self.assertEqual([item["source_key"] for item in plan["members"]], ["TEST-2"])
        self.assertTrue(any(row["issue"] == "membership_precedes_item_creation" for row in audit["membership_evidence"]))

    def test_jira_ids_are_not_confused_with_dataset_ids(self):
        self.mutate("UPDATE event SET to_value=NULL WHERE field IN ('Epic Child','Epic Link') AND to_id IN ('501','502')")
        plan, _, _ = self.read()
        self.assertEqual([item["source_key"] for item in plan["members"]], ["TEST-2"])

    def test_ambiguous_membership_is_excluded(self):
        self.mutate("INSERT INTO event VALUES ('ambiguous-membership','tawos-v1.1:2','2014-01-02T00:00:00.000000Z','membership_changed','Epic Link','TEST-1',NULL,'501',NULL)")
        plan, audit, _ = self.read()
        self.assertEqual(plan["members"], [])
        self.assertTrue(any(row["issue"] == "conflicting_membership_at_same_time" for row in audit["membership_evidence"]))

    def test_replay_is_read_only_and_outputs_are_separate(self):
        before = hashlib.sha256(self.database.read_bytes()).hexdigest()
        output = self.root / "replay"
        result = write_replay(self.database, "TEST-1", CUTOFF, output)
        self.assertEqual(result["members"], 1)
        self.assertEqual(hashlib.sha256(self.database.read_bytes()).hexdigest(), before)
        self.assertEqual({path.name for path in output.iterdir()}, {"plan.json", "audit.json", "outcome.json"})
        with self.assertRaisesRegex(ValueError, "already exists"):
            write_replay(self.database, "TEST-1", CUTOFF, output)
        with self.assertRaisesRegex(ValueError, "did not exist"):
            self.read("2013-12-31")
