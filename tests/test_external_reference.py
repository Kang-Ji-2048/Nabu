import hashlib
from contextlib import closing
import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('external_reference', ROOT/'scripts/prepare-external-reference.py')
external = importlib.util.module_from_spec(spec)
spec.loader.exec_module(external)


class ExternalReferenceTests(unittest.TestCase):
    def test_fixed_roster_is_bound_and_never_becomes_training_input(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dbpath = root/'external.sqlite'
            with closing(sqlite3.connect(dbpath)) as db, db:
                db.execute('CREATE TABLE project(source_key TEXT)')
                db.execute("INSERT INTO project VALUES ('MESOS')")
                db.execute('CREATE TABLE work_item(id TEXT,source_key TEXT)')
                db.execute("INSERT INTO work_item VALUES ('external','MESOS-1')")
            roster = root/'roster'
            roster.mkdir()
            locator = {'id': 'MESOS-1', 'epic': 'MESOS-1', 'item_id': 'external', 'as_of': '2020-01-01', 'split': 'external_test'}
            raw = json.dumps(locator)+'\n'
            (roster/'case-roster.jsonl').write_bytes(raw.encode())
            protocol = {'project': 'MESOS', 'sample_cases': 1, 'roster_sha256': hashlib.sha256(raw.encode()).hexdigest()}
            (roster/'protocol.json').write_text(json.dumps(protocol))
            development = root/'dev.jsonl'
            dev = {'split': 'train', 'as_of': '2019-01-01', 'input': {'plan': {'root': {'id': 'XD'}, 'members': []}, 'prior_work': []}}
            development.write_text(json.dumps(dev))
            item = {'id': 'external', 'source_key': 'MESOS-1', 'created_at': '2019-12-31',
                    'fields': {'title': 'A test plan', 'description': None}, 'unknown_fields': ['description']}
            frozen = {'plan': {'root': item, 'members': [], 'as_of': '2020-01-01T00:00:00.000000Z'},
                      'corpus': {}, 'evidence_fingerprint': 'fixture'}
            with patch.object(external, 'freeze_evidence', return_value=frozen) as freeze:
                external.prepare(dbpath, roster, root/'out', development, ['scope_gap'])
                self.assertEqual(freeze.call_count, 1)
                draft = json.loads((root/'out/case-drafts.jsonl').read_text())
                self.assertEqual(draft['split'], 'external_test')
                self.assertNotIn('target', draft)
                (roster/'case-roster.jsonl').write_bytes((raw+' ').encode())
                with self.assertRaisesRegex(ValueError, 'roster changed'):
                    external.prepare(dbpath, roster, root/'bad', development, ['scope_gap'])
                self.assertFalse((root/'bad').exists())

    def test_overlap_and_early_test_cases_fail_before_reconstruction(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dbpath = root/'external.sqlite'
            with closing(sqlite3.connect(dbpath)) as db, db:
                db.execute('CREATE TABLE project(source_key TEXT)')
                db.execute("INSERT INTO project VALUES ('MESOS')")
                db.execute('CREATE TABLE work_item(id TEXT,source_key TEXT)')
                db.execute("INSERT INTO work_item VALUES ('external','MESOS-1')")
            locator = {'id': 'MESOS-1', 'epic': 'MESOS-1', 'item_id': 'external', 'as_of': '2010-01-01', 'split': 'external_test'}
            raw = json.dumps(locator)+'\n'
            (root/'case-roster.jsonl').write_bytes(raw.encode())
            (root/'protocol.json').write_text(json.dumps({'project': 'MESOS', 'sample_cases': 1,
                                                         'roster_sha256': hashlib.sha256(raw.encode()).hexdigest()}))
            dev = {'split': 'train', 'as_of': '2019-01-01', 'input': {'plan': {'root': {'id': 'external'}, 'members': []}, 'prior_work': []}}
            path = root/'dev.jsonl'
            path.write_text(json.dumps(dev))
            with patch.object(external, 'freeze_evidence') as freeze:
                with self.assertRaisesRegex(ValueError, 'overlaps development'):
                    external.prepare(dbpath, root, root/'overlap', path, ['scope_gap'])
                dev['input']['plan']['root']['id'] = 'XD'
                path.write_text(json.dumps(dev))
                with self.assertRaisesRegex(ValueError, 'predates development'):
                    external.prepare(dbpath, root, root/'early', path, ['scope_gap'])
                freeze.assert_not_called()
