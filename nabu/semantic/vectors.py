import hashlib
import json
from pathlib import Path
import sqlite3

import numpy as np

from ..text import text_of


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def normalize(matrix):
    matrix = np.asarray(matrix, dtype=np.float32)
    if matrix.ndim != 2 or not matrix.shape[1] or not np.isfinite(matrix).all():
        raise ValueError("Embedding matrix must be finite, two-dimensional and nonempty")
    lengths = np.linalg.norm(matrix, axis=1, keepdims=True)
    if np.any(lengths <= 0):
        raise ValueError("Embedding model returned a zero vector")
    return matrix / lengths


def embed_items(items, encoder, cache: Path, *, embedding_batch_size=128):
    """Content-addressed cache: no IDs, outcomes or category names affect vectors."""
    ids = sorted(items)
    texts = [text_of(items[item_id]) for item_id in ids]
    if not ids or any(not text.strip() for text in texts):
        raise ValueError("Every indexed ticket must have recoverable nonempty text")
    if embedding_batch_size < 1:
        raise ValueError("Embedding batch size must be positive")
    cache.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(cache)
    try:
        connection.execute("CREATE TABLE IF NOT EXISTS embedding (model TEXT, text_hash TEXT, vector TEXT NOT NULL, PRIMARY KEY(model,text_hash))")
        keys = [digest(text) for text in texts]
        vectors, missing = {}, {}
        for key, text in zip(keys, texts):
            row = connection.execute("SELECT vector FROM embedding WHERE model=? AND text_hash=?", (encoder.fingerprint, key)).fetchone()
            if row:
                vectors[key] = json.loads(row[0])
            else:
                missing[key] = text
        # Similar lengths reduce padding; commit each batch so failures retain work.
        pending = sorted(missing, key=lambda key: (len(missing[key]), key))
        for start in range(0, len(pending), embedding_batch_size):
            batch = pending[start:start + embedding_batch_size]
            computed = normalize(encoder.documents([missing[key] for key in batch]))
            if len(computed) != len(batch):
                raise ValueError("Embedding model returned the wrong number of vectors")
            for key, vector in zip(batch, computed):
                value = vector.tolist()
                connection.execute("INSERT INTO embedding VALUES (?,?,?)", (encoder.fingerprint, key, json.dumps(value)))
                vectors[key] = value
            connection.commit()
        matrix = normalize([vectors[key] for key in keys])
    finally:
        connection.close()
    return {"ids": ids, "vectors": matrix.tolist(), "encoder": encoder.metadata,
            "text_fingerprints": dict(zip(ids, keys)), "new_embeddings": len(missing),
            "corpus_fingerprint": digest({item_id: items[item_id] for item_id in ids})}


def semantic_search(index, items, query, encoder, *, limit=5, completed_only=True):
    if encoder.fingerprint != index["encoder"]["fingerprint"]:
        raise ValueError("Embedding model assets changed; rebuild the index")
    if set(index["ids"]) != set(items) or index["corpus_fingerprint"] != digest(items):
        raise ValueError("Semantic index does not match this frozen evidence corpus")
    query_vector = normalize(encoder.query(query))[0]
    matrix = np.asarray(index["vectors"], dtype=np.float32)
    if matrix.ndim != 2 or matrix.shape[1] != len(query_vector):
        raise ValueError("Query and index dimensions differ")
    scores = matrix @ query_vector
    results = []
    for position, item_id in enumerate(index["ids"]):
        item = items[item_id]
        if completed_only and ("status" in item["unknown_fields"] or str(item["fields"]["status"]).casefold() not in {"done", "closed", "resolved"}):
            continue
        results.append((float(scores[position]), item["source_key"], item_id))
    results.sort(key=lambda value: (-value[0], value[1]))
    return [{"item": items[item_id], "similarity": score} for score, _, item_id in results[:limit]]
