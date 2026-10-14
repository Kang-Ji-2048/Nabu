"""Batch category discovery; clusters describe work, never inferred risk."""
from collections import defaultdict
import importlib.metadata
import json
from pathlib import Path
import sqlite3

import numpy as np
from sklearn.cluster import HDBSCAN
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer

from ..replay import HistoricalReader
from ..text import bounded_item, text_of
from .encoder import LocalEncoder, DEFAULT_MODEL_DIR
from .vectors import digest, embed_items, normalize, semantic_search


def project_items(database: Path, project_key: str, cutoff=None):
    connection = sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        projects = connection.execute("SELECT * FROM project WHERE source_key=?", (project_key,)).fetchall()
        if len(projects) != 1:
            raise ValueError("Expected exactly one matching project")
        rows = [dict(row) for row in connection.execute("SELECT * FROM work_item WHERE project_id=? ORDER BY created_at,id", (projects[0]["id"],))]
        if not rows:
            raise ValueError("Project has no tickets")
        if cutoff is not None:
            reader = HistoricalReader(database, rows[0]["source_key"], cutoff)
            try:
                items = {}
                for item in reader.items.values():
                    if item["created_at"] <= reader.cutoff:
                        historical, _ = reader.item_at(item["id"])
                        if text_of(historical).strip():
                            items[item["id"]] = bounded_item(historical)
                context = {"mode": "historical", "as_of": reader.cutoff, "project": project_key}
            finally:
                reader.close()
        else:
            items = {}
            for row in rows:
                item = {"id": row["id"], "source_key": row["source_key"], "created_at": row["created_at"],
                        "fields": {name: row[name] for name in ("title", "description", "type", "status", "estimate")}, "unknown_fields": []}
                if text_of(item).strip():
                    items[item["id"]] = bounded_item(item)
            context = {"mode": "current_snapshot", "as_of": None, "project": project_key,
                       "warning": "Current text may contain later edits; never reuse this category inventory in a historical review."}
        if not items:
            raise ValueError("No eligible ticket text is available")
        return items, context
    finally:
        connection.close()


def discover(items, index, *, min_cluster_size=15, min_samples=5):
    if min_cluster_size < 2 or min_samples < 1:
        raise ValueError("Cluster size must be >=2 and min_samples >=1")
    ids = index["ids"]
    if set(ids) != set(items) or index["corpus_fingerprint"] != digest(items):
        raise ValueError("Category input does not match its vector index")
    matrix = normalize(index["vectors"])
    dimensions = min(32, matrix.shape[1], len(ids)-1)
    labels = np.full(len(ids), -1, dtype=int)
    if len(ids) >= max(min_cluster_size, min_samples + 1):
        reduced = PCA(n_components=dimensions, svd_solver="full").fit_transform(matrix)
        if np.all(np.linalg.norm(reduced, axis=1) > 1e-10):
            cluster_input = normalize(reduced)
        else:
            cluster_input = matrix
        labels = HDBSCAN(min_cluster_size=min_cluster_size, min_samples=min_samples,
                         metric="euclidean", cluster_selection_method="leaf", n_jobs=2, copy=False).fit_predict(cluster_input)
    groups = defaultdict(list)
    for position, label in enumerate(labels):
        if label >= 0:
            groups[int(label)].append(position)
    ordered = sorted(groups.values(), key=lambda positions: ids[min(positions)])
    keywords = {}
    if ordered:
        # Titles explain the work; long traces/configuration often swamp descriptions.
        texts = []
        for item_id in ids:
            item = items[item_id]
            title = item["fields"]["title"] if "title" not in item["unknown_fields"] else None
            texts.append(title if isinstance(title, str) and title.strip() else text_of(item))
        try:
            vectorizer = CountVectorizer(stop_words="english", ngram_range=(1, 2), max_features=8000,
                                         token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9_-]+\b")
            counts = vectorizer.fit_transform(texts)
            aggregate = np.vstack([np.asarray(counts[positions].sum(axis=0)).ravel() for positions in ordered])
            frequency = aggregate.sum(axis=0)
            average_length = max(float(aggregate.sum(axis=1).mean()), 1)
            scores = aggregate / np.maximum(aggregate.sum(axis=1, keepdims=True), 1) * np.log1p(average_length / np.maximum(frequency, 1))
            words = vectorizer.get_feature_names_out()
            for group, row in enumerate(scores):
                keywords[group] = [str(words[pos]) for pos in np.argsort(-row, kind="stable")[:6] if row[pos] > 0]
        except ValueError:
            # A corpus containing only stopwords has no usable keyword vocabulary.
            keywords = {}
    categories, assignments = [], {item_id: None for item_id in ids}
    for group, positions in enumerate(ordered):
        members = [ids[position] for position in positions]
        category_id = "category-" + digest(members)[:12]
        centroid = normalize([matrix[positions].mean(axis=0)])[0]
        similarities = matrix[positions] @ centroid
        representatives = [members[int(pos)] for pos in np.argsort(-similarities, kind="stable")[:4]]
        words = keywords.get(group, [])
        categories.append({"id": category_id, "keyword_label": " / ".join(words[:3]) or "Unlabelled topic",
                           "keywords": words, "member_ids": members, "representative_ids": representatives,
                           "centroid": centroid.tolist(), "review_status": "unreviewed",
                           "interpretation": "Work similarity only; not a delivery-risk label."})
        assignments.update({item_id: category_id for item_id in members})
    return {"categories": categories, "assignments": assignments,
            "noise_ids": [item_id for item_id, category in assignments.items() if category is None],
            "parameters": {"algorithm": "PCA-normalize-HDBSCAN", "components": dimensions,
                           "min_cluster_size": min_cluster_size, "min_samples": min_samples,
                           "label_method": "title-first-ctfidf-v1",
                           "cluster_selection_method": "leaf", "sklearn_version": importlib.metadata.version("scikit-learn")}}


def match_categories(index, discovery, query, encoder, limit=3):
    if index["encoder"]["fingerprint"] != encoder.fingerprint:
        raise ValueError("Embedding model assets changed")
    vector = normalize(encoder.query(query))[0]
    matches = [{"id": category["id"], "keyword_label": category["keyword_label"],
                "similarity": float(np.dot(vector, category["centroid"])),
                "member_count": len(category["member_ids"]), "representative_ids": category["representative_ids"]}
               for category in discovery["categories"]]
    matches.sort(key=lambda match: (-match["similarity"], match["id"]))
    return {"matches": matches[:limit], "status": "candidate_matches_only",
            "coverage": {"indexed_tickets": len(index["ids"]),
                         "assigned_tickets": len(index["ids"]) - len(discovery["noise_ids"]),
                         "unassigned_tickets": len(discovery["noise_ids"])},
            "interpretation": "Cosine similarity is not a calibrated probability or confirmed classification."}


def write_discovery(database, project, output, *, cutoff=None, model_dir=DEFAULT_MODEL_DIR,
                    cache=Path("data/semantic/embeddings.sqlite"), min_cluster_size=15, min_samples=5,
                    encoder=None):
    if output.exists() and any(output.iterdir()):
        raise ValueError("Choose a new category version directory; prior inventories are preserved")
    if cache.resolve() == database.resolve():
        raise ValueError("Embedding cache must differ from the source database")
    items, context = project_items(database, project, cutoff)
    encoder = encoder or LocalEncoder(model_dir)
    index = embed_items(items, encoder, cache)
    discovery = discover(items, index, min_cluster_size=min_cluster_size, min_samples=min_samples)
    version = digest({"context": context, "corpus": index["corpus_fingerprint"],
                      "model": encoder.fingerprint, "parameters": discovery["parameters"]})
    output.mkdir(parents=True, exist_ok=True)
    metadata = {"format": "nabu.categories.v1", "version": version, "context": context,
                "encoder": encoder.metadata, "ids": index["ids"], "text_fingerprints": index["text_fingerprints"],
                "corpus_fingerprint": index["corpus_fingerprint"], "new_embeddings": index["new_embeddings"]}
    (output / "manifest.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    (output / "categories.json").write_text(json.dumps(discovery, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "tickets.json").write_text(json.dumps(items, ensure_ascii=False) + "\n", encoding="utf-8")
    np.savez_compressed(output / "vectors.npz", vectors=np.asarray(index["vectors"], dtype=np.float32))
    summaries = [f"# Discovered work categories: {project}", "", f"Version: {version}", "",
                 f"{len(items)} tickets; {len(discovery['categories'])} proposed categories; {len(discovery['noise_ids'])} unassigned tickets.", "",
                 "Names are unreviewed keywords. These categories describe work, not delivery risks.", ""]
    for category in sorted(discovery["categories"], key=lambda category: -len(category["member_ids"])):
        summaries.extend([f"## {category['keyword_label']} ({len(category['member_ids'])} tickets)", ""])
        for item_id in category["representative_ids"]:
            item = items[item_id]
            summaries.append(f"- {item['source_key']}: {str(item['fields']['title'] or '(unknown title)').replace(chr(10), ' ')[:180]}")
        summaries.append("")
    (output / "summary.md").write_text("\n".join(summaries), encoding="utf-8")
    return {"version": version, "context": context, "tickets": len(items),
            "categories": len(discovery["categories"]), "unassigned": len(discovery["noise_ids"]),
            "new_embeddings": index["new_embeddings"], "output": str(output.resolve())}


def search_inventory(directory: Path, query: str, *, limit=5):
    if not query.strip() or not 1 <= limit <= 20:
        raise ValueError("Search requires nonempty text and limit 1..20")
    metadata = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    items = json.loads((directory / "tickets.json").read_text(encoding="utf-8"))
    discovery = json.loads((directory / "categories.json").read_text(encoding="utf-8"))
    with np.load(directory / "vectors.npz", allow_pickle=False) as arrays:
        index = {**metadata, "vectors": arrays["vectors"].tolist()}
    encoder = LocalEncoder(Path(metadata["encoder"]["model_dir"]))
    return {"context": metadata["context"], "categories": match_categories(index, discovery, query, encoder),
            "similar_tickets": semantic_search(index, items, query, encoder, limit=limit, completed_only=False)}
