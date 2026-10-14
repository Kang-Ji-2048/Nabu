import json
from pathlib import Path
import tempfile
import unittest

import numpy as np

from nabu.semantic.categories import discover, match_categories, project_items, write_discovery
from nabu.semantic.vectors import embed_items, normalize, semantic_search
from nabu.pipeline import load


class FakeEncoder:
    """A controlled vector space for tests, not a real embedding model."""
    def __init__(self, fingerprint="test-encoder-v1"):
        self.fingerprint = fingerprint
        self.encoded_documents = 0

    @property
    def metadata(self):
        return {"model": "test-only", "fingerprint": self.fingerprint}

    def vector(self, text):
        text = text.casefold()
        group = 1 if any(word in text for word in ("schema", "sql", "ddl")) else 2 if any(word in text for word in ("identity", "auth", "login")) else 0
        import hashlib
        seed = int(hashlib.sha256(text.encode()).hexdigest()[:8], 16)
        vector = np.random.default_rng(seed).uniform(0, .01, 4)
        vector[group] += 1
        return vector

    def documents(self, texts):
        self.encoded_documents += len(texts)
        return np.asarray([self.vector(text) for text in texts])

    def query(self, text):
        return np.asarray([self.vector(text)])


def ticket(number, title, status="Done"):
    return {"id": f"tawos-v1.1:{number}", "source_key": f"TEST-{number}",
            "created_at": "2013-01-01T00:00:00.000000Z",
            "fields": {"title": title, "description": "", "type": "task", "status": status, "estimate": 3},
            "unknown_fields": []}


class SemanticTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.cache = self.root / "vectors.sqlite"
        self.encoder = FakeEncoder()

    def test_semantic_search_can_match_without_lexical_overlap(self):
        items = {item["id"]: item for item in [ticket(1, "Schema migration"), ticket(2, "Package modules")]}
        index = embed_items(items, self.encoder, self.cache)
        results = semantic_search(index, items, "DDL upgrade", self.encoder, limit=1)
        self.assertEqual(results[0]["item"]["source_key"], "TEST-1")

    def test_cache_reuses_unchanged_text_and_invalidates_changed_text_and_model(self):
        items = {"tawos-v1.1:1": ticket(1, "Schema migration")}
        self.assertEqual(embed_items(items, self.encoder, self.cache)["new_embeddings"], 1)
        self.assertEqual(embed_items(items, self.encoder, self.cache)["new_embeddings"], 0)
        items["tawos-v1.1:1"]["fields"]["title"] = "Schema migration with compatibility"
        self.assertEqual(embed_items(items, self.encoder, self.cache)["new_embeddings"], 1)
        self.assertEqual(embed_items(items, FakeEncoder("new-model"), self.cache)["new_embeddings"], 1)

    def test_failed_embedding_batch_retains_completed_batches_for_resume(self):
        class FailingEncoder(FakeEncoder):
            calls = 0
            def documents(self, texts):
                self.calls += 1
                if self.calls == 2:
                    raise RuntimeError("interrupted inference")
                return super().documents(texts)
        items = {item["id"]: item for item in [ticket(i, f"Schema migration {i}") for i in range(5)]}
        with self.assertRaisesRegex(RuntimeError, "interrupted inference"):
            embed_items(items, FailingEncoder(), self.cache, embedding_batch_size=2)
        resumed = embed_items(items, self.encoder, self.cache, embedding_batch_size=2)
        self.assertEqual(resumed["new_embeddings"], 3)
        self.assertEqual(self.encoder.encoded_documents, 3)
        results = semantic_search(resumed, items, "DDL upgrade", self.encoder)
        self.assertEqual(len(results), 5)

    def test_snapshot_index_cannot_be_reused_against_a_different_historical_corpus(self):
        items = {item["id"]: item for item in [ticket(1, "Schema migration"), ticket(2, "Future modules")]}
        index = embed_items(items, self.encoder, self.cache)
        with self.assertRaisesRegex(ValueError, "frozen evidence corpus"):
            semantic_search(index, {"tawos-v1.1:1": items["tawos-v1.1:1"]}, "DDL", self.encoder)
        with self.assertRaisesRegex(ValueError, "assets changed"):
            semantic_search(index, items, "DDL", FakeEncoder("different-model"))

    def test_done_filter_uses_only_known_historical_status(self):
        known = ticket(1, "Schema migration", "To Do")
        unknown = ticket(2, "Schema migration compatibility")
        unknown["unknown_fields"] = ["status"]
        items = {known["id"]: known, unknown["id"]: unknown}
        index = embed_items(items, self.encoder, self.cache)
        self.assertEqual(semantic_search(index, items, "DDL", self.encoder), [])
        self.assertEqual(len(semantic_search(index, items, "DDL", self.encoder, completed_only=False)), 2)

    def test_too_little_evidence_is_left_unassigned(self):
        items = {"tawos-v1.1:1": ticket(1, "Schema migration")}
        index = embed_items(items, self.encoder, self.cache)
        result = discover(items, index, min_cluster_size=3)
        self.assertEqual(result["categories"], [])
        self.assertEqual(result["noise_ids"], ["tawos-v1.1:1"])
        self.assertIsNone(result["assignments"]["tawos-v1.1:1"])
        self.assertEqual(len(semantic_search(index, items, "DDL", self.encoder)), 1)

    def test_batch_refresh_can_discover_a_new_category_without_fixed_k(self):
        items = {}
        for group, word in enumerate(("Module packaging", "SQL schema", "Login identity")):
            for offset in range(10):
                item = ticket(group*10+offset+1, f"{word} variation {offset}")
                items[item["id"]] = item
        initial = {key: item for key, item in items.items() if int(key.split(":")[-1]) <= 20}
        first = discover(initial, embed_items(initial, self.encoder, self.cache), min_cluster_size=8, min_samples=2)
        second_index = embed_items(items, self.encoder, self.cache)
        second = discover(items, second_index, min_cluster_size=8, min_samples=2)
        self.assertEqual(len(first["categories"]), 2)
        self.assertEqual(len(second["categories"]), 3)
        self.assertEqual(sum(len(category["member_ids"]) for category in second["categories"]) + len(second["noise_ids"]), 30)
        result = match_categories(second_index, second, "authentication", self.encoder)
        self.assertEqual(result["status"], "candidate_matches_only")
        self.assertTrue(all(category["review_status"] == "unreviewed" for category in second["categories"]))

    def test_invalid_vectors_fail_instead_of_polluting_index(self):
        for values in ([[0, 0]], [[float("nan"), 1]], [1, 2]):
            with self.assertRaises(ValueError):
                normalize(values)

    def test_historical_category_corpus_excludes_later_text_and_new_tickets(self):
        database = self.root / "source.sqlite"
        records = [{"table": "Project", "row": {"ID": 1, "Project_Key": "TEST"}}]
        for iid, created in ((1, "2014-01-01"), (2, "2014-01-10")):
            records.append({"table": "Issue", "row": {"ID": iid, "Project_ID": 1, "Issue_Key": f"TEST-{iid}",
                "Title": "FUTURE_SECRET", "Description": "FUTURE_SECRET", "Type": "Task", "Status": "Done",
                "Creation_Date": created, "Last_Updated": "2014-01-20"}})
        records.append({"table": "Change_Log", "row": {"ID": 1, "Issue_ID": 1, "Field": "summary",
            "Creation_Date": "2014-01-20", "From_String": "Original schema work", "To_String": "FUTURE_SECRET"}})
        source = self.root / "source.jsonl"
        source.write_text("\n".join(json.dumps(row) for row in records))
        load(source, database)
        items, context = project_items(database, "TEST", "2014-01-05")
        self.assertEqual(set(items), {"tawos-v1.1:1"})
        self.assertNotIn("FUTURE_SECRET", json.dumps(items))
        self.assertEqual(context["mode"], "historical")
        output = self.root / "inventory-v1"
        result = write_discovery(database, "TEST", output, cutoff="2014-01-05", encoder=self.encoder, cache=self.cache)
        self.assertEqual(result["tickets"], 1)
        with self.assertRaisesRegex(ValueError, "new category version"):
            write_discovery(database, "TEST", output, encoder=self.encoder, cache=self.cache)
