import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from nabu.pipeline import load


FIXTURE = Path(__file__).parent / "fixtures" / "tawos-synthetic.jsonl"


class PipelineTests(unittest.TestCase):
    def test_outcomes_are_not_normalized_as_planned_estimates_or_status(self):
        source = self.variant(extra=[
            {"table": "Change_Log", "row": {"ID": 102, "Issue_ID": 10, "Field": "Actual Story Points", "Change_Type": "STORY_POINT", "Creation_Date": "2021-01-15", "To_String": "8"}},
            {"table": "Change_Log", "row": {"ID": 103, "Issue_ID": 10, "Field": "resolution", "Change_Type": "STATUS", "Creation_Date": "2021-01-15", "To_String": "Fixed"}},
        ])
        self.assertEqual(load(source, self.database)["rejected"], 0)
        self.assertEqual(self.query("SELECT kind,count(*) FROM event GROUP BY kind ORDER BY kind"), [
            ("actual_estimate_changed", 1), ("estimate_changed", 1),
            ("resolution_changed", 1), ("status_changed", 1),
        ])

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.database = self.root / "nabu.sqlite"

    def query(self, sql):
        connection = sqlite3.connect(self.database)
        try:
            return connection.execute(sql).fetchall()
        finally:
            connection.close()

    def variant(self, *, extra=(), transform=None):
        records = [json.loads(line) for line in FIXTURE.read_text().splitlines()]
        if transform:
            records = transform(records)
        path = self.root / "variant.jsonl"
        path.write_text("\n".join(json.dumps(row) for row in [*records, *extra]), encoding="utf-8")
        return path

    def test_end_to_end_and_repeat_load(self):
        for _ in range(2):
            report = load(FIXTURE, self.database)
            self.assertEqual(report["rejected"], 0)
            self.assertEqual(report["loaded"]["Issue"], 2)
        self.assertEqual(self.query("SELECT count(*) FROM work_item"), [(2,)])
        self.assertEqual(self.query("SELECT count(*) FROM event"), [(2,)])
        self.assertEqual(self.query("SELECT count(*) FROM raw_record"), [(9,)])
        self.assertEqual(self.query("SELECT from_id,to_id,kind FROM link"), [("tawos-v1.1:11", "tawos-v1.1:10", "blocks")])
        self.assertEqual(self.query("SELECT estimate FROM work_item WHERE source_key='DEMO-2'"), [(0.0,)])
        self.assertEqual(self.query("SELECT created_at,snapshot_only FROM work_item LIMIT 1"), [("2021-01-01T09:00:00.000000Z", 1)])
        self.assertEqual(self.query("SELECT count(*) FROM ingestion_run WHERE status='completed'"), [(2,)])

    def test_rejections_and_unknown_values_are_observable(self):
        def change(records):
            records[1]["row"]["Status"] = "Awaiting banana"
            records[1]["row"]["Type"] = "Feature"
            records[5]["row"]["Description"] = "custom relationship"
            return records
        source = self.variant(transform=change, extra=[
            {"table": "Issue", "row": {"ID": 99, "Project_ID": 1}},
            {"table": "Change_Log", "row": {"ID": 102, "Issue_ID": 999, "Field": "status", "Creation_Date": "2021-01-01"}},
            {"table": "Issue", "row": {"ID": 10}},
        ])
        with source.open("a") as stream:
            stream.write("\n{broken")
        report = load(source, self.database)
        self.assertEqual(report["rejected"], 4)
        self.assertEqual(report["unmapped_statuses"], {"Awaiting banana": 1})
        self.assertEqual(report["unmapped_types"], {"Feature": 1})
        self.assertEqual(report["unmapped_links"], {"custom relationship": 1})
        self.assertEqual(self.query("SELECT count(*) FROM rejected_record"), [(4,)])
        self.assertEqual(self.query("SELECT type,status_category FROM work_item WHERE source_key='DEMO-1'"), [("unknown", "unknown")])

    def test_input_order_does_not_matter(self):
        source = self.variant(transform=lambda records: list(reversed(records)))
        self.assertEqual(load(source, self.database)["rejected"], 0)

    def test_new_snapshot_removes_deleted_rows(self):
        load(FIXTURE, self.database)
        source = self.variant(transform=lambda records: [r for r in records if r["table"] != "Change_Log"])
        load(source, self.database)
        self.assertEqual(self.query("SELECT count(*) FROM event"), [(0,)])

    def test_fatal_load_preserves_previous_snapshot(self):
        load(FIXTURE, self.database)
        source = self.variant(transform=lambda records: [r for r in records if r["table"] == "Project"])
        with self.assertRaisesRegex(ValueError, "at least one valid"):
            load(source, self.database)
        self.assertEqual(self.query("SELECT count(*) FROM work_item"), [(2,)])
        self.assertEqual(self.query("SELECT count(*) FROM ingestion_run WHERE status='failed'"), [(1,)])

    def test_bad_estimates_and_dates_are_rejected(self):
        for value in (-1, "NaN", "Infinity", True, "banana"):
            def change(records):
                records[1]["row"]["Story_Point"] = value
                return records
            report = load(self.variant(transform=change), self.database)
            self.assertEqual(report["loaded"]["Issue"], 1)
            self.assertGreater(report["rejected"], 0)
        def bad_date(records):
            records[1]["row"]["Resolution_Date"] = "2000-01-01"
            return records
        self.assertGreater(load(self.variant(transform=bad_date), self.database)["rejected"], 0)

    def test_external_reversed_link_is_preserved(self):
        def change(records):
            records[5]["row"]["Target_Issue_ID"] = 999
            return records
        report = load(self.variant(transform=change), self.database)
        self.assertEqual(report["external_links"], 1)
        self.assertEqual(report["rejected"], 0)
        self.assertEqual(self.query("SELECT from_id,to_id FROM link"), [("tawos-v1.1:999", "tawos-v1.1:10")])

    def test_dependency_direction_from_real_tawos_phrases(self):
        for phrase, expected in [
            ("depends on", ("tawos-v1.1:11", "tawos-v1.1:10")),
            ("is depended on by", ("tawos-v1.1:10", "tawos-v1.1:11")),
        ]:
            def change(records):
                records[5]["row"]["Description"] = phrase
                return records
            self.assertEqual(load(self.variant(transform=change), self.database)["rejected"], 0)
            self.assertEqual(self.query("SELECT from_id,to_id FROM link WHERE kind='blocks'"), [expected])

    def test_loading_another_project_preserves_first_project(self):
        load(FIXTURE, self.database)
        second = self.root / "second.jsonl"
        second.write_text("\n".join(json.dumps(row) for row in [
            {"table": "Project", "row": {"ID": 2, "Project_Key": "SECOND"}},
            {"table": "Issue", "row": {"ID": 999, "Project_ID": 2, "Issue_Key": "SECOND-1", "Title": "Other project", "Creation_Date": "2021-01-01", "Status": "Open", "Type": "Task"}},
        ]))
        load(second, self.database)
        self.assertEqual(self.query("SELECT count(*) FROM project"), [(2,)])
        self.assertEqual(self.query("SELECT count(*) FROM work_item"), [(3,)])
        self.assertEqual(self.query("SELECT count(*) FROM event"), [(2,)])


if __name__ == "__main__":
    unittest.main()
