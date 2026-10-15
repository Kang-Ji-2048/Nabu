import json
from contextlib import closing
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/prepare-external-test.py'


class ExternalTestIsolationTests(unittest.TestCase):
    def test_metadata_only_selection_is_deterministic_and_rejects_overlap(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            db_path = root / 'source.sqlite'
            # No title, description or outcome columns: selection cannot read them.
            with closing(sqlite3.connect(db_path)) as db, db:
                db.execute('CREATE TABLE project(id TEXT,source_key TEXT)')
                db.execute("INSERT INTO project VALUES ('external','MESOS')")
                db.execute('CREATE TABLE work_item(id TEXT,source_key TEXT,project_id TEXT,created_at TEXT,type TEXT)')
                for i in range(40):
                    db.execute('INSERT INTO work_item VALUES (?,?,?,?,?)', (f'item-{i}', f'MESOS-{i}', 'external', '2016-01-01T00:00:00.000000Z', 'epic'))
                db.execute("INSERT INTO work_item VALUES ('early','MESOS-E','external','2010-01-01T00:00:00.000000Z','epic')")
            labels_path = root / 'development.jsonl'
            labels = {'split': 'train', 'as_of': '2015-01-01', 'input': {'plan': {'root': {'id': 'XD-root'}, 'members': []}, 'prior_work': []}}
            labels_path.write_text(json.dumps(labels))
            def invoke(output):
                return subprocess.run([sys.executable, str(SCRIPT), '--database', str(db_path), '--project', 'MESOS', '--development-labels', str(labels_path), '--output', str(output)], capture_output=True, text=True)
            one, two = root / 'one', root / 'two'
            self.assertEqual(invoke(one).returncode, 0)
            self.assertEqual(invoke(two).returncode, 0)
            self.assertEqual((one / 'case-roster.jsonl').read_bytes(), (two / 'case-roster.jsonl').read_bytes())
            roster = [json.loads(line) for line in (one / 'case-roster.jsonl').read_text().splitlines()]
            self.assertEqual(len(roster), 32)
            self.assertNotIn('early', {row['item_id'] for row in roster})
            labels['input']['prior_work'] = [{'id': 'item-1'}]
            labels_path.write_text(json.dumps(labels))
            blocked = invoke(root / 'blocked')
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn('overlaps', blocked.stderr)
            self.assertFalse((root / 'blocked').exists())
