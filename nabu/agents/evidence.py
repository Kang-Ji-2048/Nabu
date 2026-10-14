import hashlib
import json
from pathlib import Path

from ..replay import HistoricalReader
from ..text import bounded_item, text_of, tokens


def freeze_evidence(database: Path, epic: str, cutoff: str, *, exclude_evidence_ids=()):
    excluded = set(exclude_evidence_ids)
    reader = HistoricalReader(database, epic, cutoff)
    try:
        plan, _ = reader.plan()
        plan = {**plan, "root": bounded_item(plan["root"]), "members": [bounded_item(item) for item in plan["members"]]}
        targets = {item["id"] for item in [plan["root"], *plan["members"]]}
        corpus, scopes = {}, {}
        for item_id, item in reader.items.items():
            if item_id in targets or item_id in excluded or item["created_at"] > reader.cutoff:
                continue
            historical, _ = reader.item_at(item_id)
            # Unknown text cannot be used to rank or justify a candidate.
            if text_of(historical).strip():
                corpus[item_id] = bounded_item(historical)
        for item_id in corpus:
            if any(event["field"].casefold() == "epic child" and event["at"] <= reader.cutoff for event in reader.events[item_id]):
                # Do not reconstruct a prior scope containing withheld references.
                # Membership checks use IDs only; underlying source tables are
                # still loaded by HistoricalReader for historical reconstruction.
                if excluded:
                    changes, _ = reader.membership_changes(item_id)
                    if excluded.intersection(changes):
                        continue
                scope, _ = reader.plan(item_id)
                scopes[item_id] = [bounded_item(member) for member in scope["members"] if member["id"] not in targets]
        payload = {"plan": plan, "corpus": corpus, "scopes": scopes}
        fingerprint = hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        return {**payload, "evidence_fingerprint": fingerprint}
    finally:
        reader.close()


def execute_tool(name, args, state, encoder=None):
    """Pure reads of a frozen historical corpus; no model-controlled SQL/cutoff."""
    corpus = state["corpus"]
    evidence = dict(state.get("evidence", {}))
    if name == "get_plan":
        return state["plan"], evidence
    if name == "search_prior_work":
        if state.get("semantic_index") is not None:
            from ..semantic.vectors import semantic_search
            if encoder is None:
                raise ValueError("The pinned local embedding model is required for semantic retrieval")
            ranked = semantic_search(state["semantic_index"], corpus, args.query, encoder,
                                     limit=args.limit, completed_only=args.completed_only)
            results = [entry["item"] for entry in ranked]
            evidence.update({item["id"]: item for item in results})
            assignments = state["category_inventory"]["assignments"]
            return {"items": results, "method": "semantic_cosine", "coverage": "recoverable_text_only",
                    "matches": [{"item_id": entry["item"]["id"], "similarity": entry["similarity"],
                                 "category_id": assignments.get(entry["item"]["id"])} for entry in ranked],
                    "interpretation": "Similarity and proposed categories do not establish delivery risk."}, evidence
        query = tokens(args.query)
        scored = []
        for item in corpus.values():
            if args.completed_only and ("status" in item["unknown_fields"] or str(item["fields"]["status"]).casefold() not in {"done", "closed", "resolved"}):
                continue
            words = tokens(text_of(item))
            overlap = len(query & words)
            if overlap:
                scored.append((overlap / max(len(query), 1), item["source_key"], item))
        scored.sort(key=lambda entry: (-entry[0], entry[1]))
        results = [item for _, _, item in scored[:args.limit]]
        evidence.update({item["id"]: item for item in results})
        return {"items": results, "method": "lexical_overlap", "coverage": "recoverable_text_only"}, evidence
    if name in {"get_item", "inspect_scope"}:
        item = corpus.get(args.item_id)
        if item is None:
            raise ValueError("Item is not in the eligible prior evidence corpus")
        evidence[item["id"]] = item
        if name == "get_item":
            return item, evidence
        members = state["scopes"].get(item["id"], [])
        evidence.update({member["id"]: member for member in members})
        return {"root": item, "members": members, "scope_coverage": "observed_membership_only",
                "membership_evidence_available": item["id"] in state["scopes"]}, evidence
    if name == "measure_pattern":
        ids = list(dict.fromkeys(args.item_ids))
        if any(item_id not in evidence for item_id in ids):
            raise ValueError("Inspect every cited item before measuring a pattern")
        matches, missing, partial = [], [], []
        for item_id in ids:
            text = text_of(evidence[item_id])
            if any(name in evidence[item_id]["unknown_fields"] for name in ("title", "description")) or evidence[item_id].get("truncated_fields"):
                partial.append(item_id)
            if not text:
                missing.append(item_id)
            elif args.term.casefold() in text.casefold():
                matches.append(item_id)
        return {"selected_count": len(ids), "matched_count": len(matches), "matching_ids": matches,
                "missing_text_ids": missing, "partial_text_ids": partial,
                "interpretation": "Selected examples only; not a calibrated risk probability."}, evidence
    raise ValueError("Unsupported tool")


def validate_findings(findings, state):
    targets = {item["id"] for item in [state["plan"]["root"], *state["plan"]["members"]]}
    valid, errors = [], []
    for finding in findings:
        problems = []
        if not set(finding["target_item_ids"]) <= targets:
            problems.append("Targets must belong to the supplied historical plan")
        cited = set()
        for citation in finding["citations"]:
            item = state["evidence"].get(citation["item_id"])
            if item is None:
                problems.append("Citation was not returned by an evidence tool")
                continue
            if item["id"] in targets or item["created_at"] > state["plan"]["as_of"]:
                problems.append("Citation is not eligible prior evidence")
                continue
            value = item["fields"].get(citation["field"])
            if citation["field"] in item["unknown_fields"] or value is None or citation["quote"] not in str(value):
                problems.append("Citation quote is not an exact excerpt of a known historical field")
            else:
                cited.add(item["id"])
        if len(cited) < 2:
            problems.append("At least two distinct prior tickets with valid quotes are required")
        if problems:
            errors.append({"finding_id": finding["id"], "reasons": sorted(set(problems))})
        else:
            valid.append(finding)
    return valid, errors
