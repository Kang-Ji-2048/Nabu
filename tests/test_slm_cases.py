from contextlib import closing
import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from nabu.agents.evidence import freeze_evidence
from nabu.pipeline import load
from nabu.replay import HistoricalReader

spec = importlib.util.spec_from_file_location('nabu_slm_cases', Path(__file__).resolve().parents[1] / 'scripts/prepare-slm-cases.py')
cases = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cases)


class DevelopmentCaseTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.database = self.root / 'source.sqlite'
        with closing(sqlite3.connect(self.database)) as db, db:
            db.executescript('''
                CREATE TABLE work_item (id TEXT,source_key TEXT,created_at TEXT,type TEXT,project_id TEXT,source TEXT);
                CREATE TABLE raw_record (source TEXT,source_id TEXT,table_name TEXT,payload TEXT);
                CREATE TABLE event (item_id TEXT,field TEXT,from_value TEXT,to_value TEXT,from_id TEXT,to_id TEXT);
            ''')
            for number in range(1, 21):
                db.execute('INSERT INTO work_item VALUES (?,?,?,?,?,?)',
                           (f'tawos:{number}', f'XD-{number}', f'2014-01-{number:02d}T00:00:00.000000Z', 'epic', 'xd', 'tawos'))
                # Extract only Jira_ID; payload text must not reach frozen inputs.
                db.execute('INSERT INTO raw_record VALUES (?,?,?,?)',
                           ('tawos', str(number), 'Issue', json.dumps({'Jira_ID': 500 + number, 'Title': 'DO_NOT_READ_HELD_OUT_TEXT'})))
        self.output = self.root / 'drafts'

    @staticmethod
    def freeze(database, epic, cutoff, *, exclude_evidence_ids=()):
        number = epic.removeprefix('XD-')
        if int(number) >= 16:
            raise AssertionError('Held-out example was reconstructed')
        item = {'id': f'tawos:{number}', 'source_key': epic,
                'created_at': f'2014-01-{int(number):02d}T00:00:00.000000Z',
                'fields': {'title': f'Historical plan {epic}', 'description': 'Supplied historical scope',
                           'status': 'To Do', 'type': 'Epic', 'estimate': None},
                'unknown_fields': []}
        # A held-out root can exist by a validation cutoff although its own
        # one-day review belongs to test. It must be withheld explicitly.
        prior = {'id': 'tawos:16', 'source_key': 'XD-16',
                 'created_at': '2014-01-16T00:00:00.000000Z',
                 'fields': {**item['fields'], 'title': 'Historical plan held-out'},
                 'unknown_fields': []}
        corpus = {} if prior['id'] in exclude_evidence_ids else {prior['id']: prior}
        return {'plan': {'root': item, 'members': [], 'as_of': cutoff},
                'corpus': corpus, 'evidence_fingerprint': f'fingerprint-{epic}'}

    def test_development_only_never_freezes_or_emits_held_out_examples(self):
        with patch.object(cases, 'freeze_evidence', side_effect=self.freeze) as freeze:
            report = cases.prepare_cases(self.database, self.output, ['scope_gap'], development_only=True)
        self.assertEqual(report['counts'], {'train': 13, 'validation': 2})
        self.assertFalse(report['held_out_reconstructed'])
        self.assertEqual([call.args[1] for call in freeze.call_args_list], [f'XD-{number}' for number in range(1, 16)])
        self.assertFalse((self.output / 'test-drafts.jsonl').exists())
        self.assertFalse((self.output / 'test-ticket-ids.jsonl').exists())
        train = [json.loads(line) for line in (self.output / 'train-drafts.jsonl').read_text().splitlines()]
        validation = [json.loads(line) for line in (self.output / 'validation-drafts.jsonl').read_text().splitlines()]
        self.assertEqual(train[0]['as_of'], '2014-01-02T00:00:00.000000Z')
        self.assertEqual(train[0]['evidence_fingerprint'], 'fingerprint-XD-1')
        self.assertEqual(train[0]['input']['allowed_risk_types'], ['scope_gap'])
        self.assertTrue(all(not row['input']['prior_work'] for row in train + validation))
        self.assertEqual(report['held_out_evidence_ids_excluded'], 5)
        self.assertTrue(all('tawos:16' in call.kwargs['exclude_evidence_ids'] for call in freeze.call_args_list))
        self.assertTrue(all(row['review_status'] == 'draft' and 'target' not in row for row in train + validation))
        self.assertEqual({row['split'] for row in validation}, {'validation'})
        self.assertNotIn('DO_NOT_READ_HELD_OUT_TEXT', ''.join(path.read_text() for path in self.output.iterdir()))

    def test_metadata_overlap_excludes_shared_train_validation_and_test_ids(self):
        with closing(sqlite3.connect(self.database)) as db, db:
            # A validation root and held-out root refer to earlier train roots.
            # Jira-ID-only references exercise mapping without raw ticket text.
            db.execute('INSERT INTO event VALUES (?,?,?,?,?,?)', ('tawos:14', 'Epic Child', None, None, None, '501'))
            db.execute('INSERT INTO event VALUES (?,?,?,?,?,?)', ('tawos:2', 'Epic Link', None, None, None, '518'))
        with patch.object(cases, 'freeze_evidence', side_effect=self.freeze) as freeze:
            report = cases.prepare_cases(self.database, self.output, ['scope_gap'], development_only=True)
        self.assertEqual(report['counts'], {'train': 11, 'validation': 1})
        self.assertEqual({row['id'] for row in report['excluded']}, {'XD-1', 'XD-2', 'XD-14'})
        self.assertEqual(report['group_check'], 'conservative_all_time_membership_reference_metadata')
        frozen_keys = {call.args[1] for call in freeze.call_args_list}
        self.assertTrue({'XD-1', 'XD-2', 'XD-14', 'XD-18'}.isdisjoint(frozen_keys))

    def test_conflicting_held_out_parent_reference_withholds_both_candidates(self):
        with closing(sqlite3.connect(self.database)) as db, db:
            db.execute('INSERT INTO event VALUES (?,?,?,?,?,?)',
                       ('tawos:18', 'Epic Child', None, 'XD-1', None, '502'))
        original_database = self.database.read_bytes()
        with patch.object(cases, 'freeze_evidence', side_effect=self.freeze) as freeze:
            report = cases.prepare_cases(self.database, self.output, ['scope_gap'], development_only=True)
        self.assertEqual(report['counts'], {'train': 11, 'validation': 2})
        self.assertEqual({row['id'] for row in report['excluded']}, {'XD-1', 'XD-2'})
        for call in freeze.call_args_list:
            self.assertTrue({'tawos:1', 'tawos:2'} <= call.kwargs['exclude_evidence_ids'])
        self.assertTrue({'XD-1', 'XD-2'}.isdisjoint(call.args[1] for call in freeze.call_args_list))
        self.assertEqual(report['membership_ambiguities'], [{
            'item_id': 'tawos:18', 'field': 'Epic Child', 'side': 'to',
            'label': 'XD-1', 'jira_id': '502', 'candidate_item_ids': ['tawos:1', 'tawos:2']}])
        self.assertEqual(self.database.read_bytes(), original_database)

    def test_conflicting_child_link_joins_every_candidate_epic(self):
        with closing(sqlite3.connect(self.database)) as db, db:
            db.execute('INSERT INTO event VALUES (?,?,?,?,?,?)',
                       ('tawos:1', 'Epic Link', None, 'XD-14', None, '518'))
        with patch.object(cases, 'freeze_evidence', side_effect=self.freeze) as freeze:
            report = cases.prepare_cases(self.database, self.output, ['scope_gap'], development_only=True)
        # The child is a train root, and both validation/test candidate parents
        # must include it: otherwise the validation parent would survive.
        self.assertEqual(report['counts'], {'train': 12, 'validation': 1})
        self.assertEqual({row['id'] for row in report['excluded']}, {'XD-1', 'XD-14'})
        self.assertTrue(all('tawos:1' in call.kwargs['exclude_evidence_ids'] for call in freeze.call_args_list))
        self.assertTrue({'XD-1', 'XD-14', 'XD-18'}.isdisjoint(call.args[1] for call in freeze.call_args_list))
        self.assertEqual(report['membership_ambiguities'][0]['candidate_item_ids'], ['tawos:14', 'tawos:18'])

    def test_unresolved_held_out_parent_reference_fails_before_reconstruction(self):
        with closing(sqlite3.connect(self.database)) as db, db:
            db.execute('INSERT INTO event VALUES (?,?,?,?,?,?)',
                       ('tawos:18', 'Epic Child', None, 'XD-MISSING', None, '9999'))
        original_database = self.database.read_bytes()
        with patch.object(cases, 'freeze_evidence') as freeze:
            with self.assertRaisesRegex(ValueError, 'Unresolved held-out Epic Child references for XD-18'):
                cases.prepare_cases(self.database, self.output, ['scope_gap'], development_only=True)
        freeze.assert_not_called()
        self.assertFalse(self.output.exists())
        self.assertEqual(list(self.root.glob('.drafts-*')), [])
        self.assertEqual(self.database.read_bytes(), original_database)

    def test_unresolved_child_link_quarantines_child_and_all_containing_plans(self):
        with closing(sqlite3.connect(self.database)) as db, db:
            db.execute('INSERT INTO event VALUES (?,?,?,?,?,?)',
                       ('tawos:1', 'Epic Link', None, 'XD-MISSING', None, '9999'))
            db.execute('INSERT INTO event VALUES (?,?,?,?,?,?)',
                       ('tawos:2', 'Epic Child', None, 'XD-1', None, '501'))
        original_database = self.database.read_bytes()

        def freeze_with_quarantined_prior(database, epic, cutoff, *, exclude_evidence_ids=()):
            frozen = self.freeze(database, epic, cutoff, exclude_evidence_ids=exclude_evidence_ids)
            if 'tawos:1' not in exclude_evidence_ids:
                # This earlier child is relevant evidence for every synthetic
                # plan, so a missing exclusion would reach the published input.
                frozen['corpus']['tawos:1'] = {
                    **frozen['plan']['root'], 'id': 'tawos:1', 'source_key': 'XD-1',
                    'created_at': '2014-01-01T00:00:00.000000Z'}
            return frozen

        with patch.object(cases, 'freeze_evidence', side_effect=freeze_with_quarantined_prior) as freeze:
            report = cases.prepare_cases(self.database, self.output, ['scope_gap'], development_only=True)
        self.assertEqual(report['counts'], {'train': 11, 'validation': 2})
        self.assertEqual({row['id'] for row in report['excluded']}, {'XD-1', 'XD-2'})
        self.assertTrue(all(row['quarantined_item_ids'] == ['tawos:1'] for row in report['excluded']))
        self.assertTrue({'XD-1', 'XD-2'}.isdisjoint(call.args[1] for call in freeze.call_args_list))
        self.assertTrue(all('tawos:1' in call.kwargs['exclude_evidence_ids'] for call in freeze.call_args_list))
        self.assertEqual(report['quarantined_child_count'], 1)
        self.assertEqual(report['quarantined_child_ids'], ['tawos:1'])
        self.assertEqual(report['held_out_evidence_ids_excluded'], 5)
        self.assertEqual(report['evidence_ids_excluded'], 6)
        drafts = [json.loads(line) for split in ('train', 'validation')
                  for line in (self.output / f'{split}-drafts.jsonl').read_text().splitlines()]
        self.assertTrue(all(not row['input']['prior_work'] for row in drafts))
        self.assertTrue(all(row['input']['plan']['root']['id'] != 'tawos:1' for row in drafts))
        self.assertEqual(self.database.read_bytes(), original_database)

    def test_failed_reconstruction_publishes_nothing(self):
        with patch.object(cases, 'freeze_evidence', side_effect=ValueError('invalid historical input')):
            with self.assertRaisesRegex(ValueError, 'invalid historical input'):
                cases.prepare_cases(self.database, self.output, ['scope_gap'], development_only=True)
        self.assertFalse(self.output.exists())
        self.assertEqual(list(self.root.glob('.drafts-*')), [])

    def test_existing_outputs_are_not_replaced(self):
        self.output.mkdir()
        marker = self.output / 'existing-labels.jsonl'
        marker.write_text('original labels')
        with patch.object(cases, 'freeze_evidence') as freeze:
            with self.assertRaisesRegex(ValueError, 'new output directory'):
                cases.prepare_cases(self.database, self.output, ['scope_gap'], development_only=True)
        freeze.assert_not_called()
        self.assertEqual(marker.read_text(), 'original labels')


class EvidenceExclusionTests(unittest.TestCase):
    def test_withheld_ticket_never_reconstructed_as_prior_item_or_scope_member(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            database = root / 'source.sqlite'
            records = [{'table': 'Project', 'row': {'ID': 1, 'Project_Key': 'XD'}}]
            for iid, kind in ((1, 'Epic'), (2, 'Story'), (3, 'Task')):
                records.append({'table': 'Issue', 'row': {
                    'ID': iid, 'Jira_ID': 500 + iid, 'Project_ID': 1,
                    'Issue_Key': f'XD-{iid}', 'Type': kind, 'Title': f'Historical ticket {iid}',
                    'Description': 'Historical supplied evidence', 'Status': 'To Do',
                    'Creation_Date': f'2014-01-0{iid}', 'Last_Updated': f'2014-01-0{iid}'}})
            records.append({'table': 'Change_Log', 'row': {
                'ID': 100, 'Issue_ID': 2, 'Field': 'Epic Child',
                'Creation_Date': '2014-01-03', 'From_String': None,
                'To_String': 'XD-3', 'To_Value': '503', 'Change_Type': 'OTHER'}})
            source = root / 'source.jsonl'
            source.write_text(''.join(json.dumps(row) + '\n' for row in records))
            self.assertEqual(load(source, database)['rejected'], 0)
            cutoff = '2014-01-05T00:00:00Z'
            default = freeze_evidence(database, 'XD-1', cutoff)
            explicit_default = freeze_evidence(database, 'XD-1', cutoff, exclude_evidence_ids=())
            self.assertEqual(default, explicit_default)
            blocked = 'tawos-v1.1:3'
            prior_root = 'tawos-v1.1:2'
            self.assertIn(blocked, default['corpus'])
            self.assertEqual([item['id'] for item in default['scopes'][prior_root]], [blocked])
            original = HistoricalReader.item_at
            visited = []

            def guarded_item_at(reader, item_id):
                self.assertNotEqual(item_id, blocked, 'Withheld historical text was reconstructed')
                visited.append(item_id)
                return original(reader, item_id)

            with patch.object(HistoricalReader, 'item_at', guarded_item_at):
                frozen = freeze_evidence(database, 'XD-1', cutoff, exclude_evidence_ids={blocked})
            self.assertNotIn(blocked, visited)
            self.assertNotIn(blocked, frozen['corpus'])
            self.assertIn(prior_root, frozen['corpus'])
            self.assertNotIn(prior_root, frozen['scopes'])
            self.assertNotIn('Historical ticket 3', json.dumps(frozen))
            payload = cases.detector_input(frozen, ['scope_gap'], 12)
            self.assertEqual([item['id'] for item in payload['prior_work']], [prior_root])
