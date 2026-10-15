"""Bounded, exact selectable text evidence for ticket risk classification."""
import hashlib
import re

from ..labelling import encode

TEXT_FIELDS = ("title", "description", "acceptance_criteria")


def classifier_payload(example):
    source = example["input"]
    focus = source["ticket"]
    context = source.get("context", {})
    all_items = [focus]
    relationships = []
    for plan in context.get("plans", []):
        all_items.extend([plan["root"], *plan["members"]])
        relationships.append({"root_id": plan["root"]["id"],
                              "member_ids": [item["id"] for item in plan["members"]],
                              "omitted_members": plan["omitted_members"]})
    unique = {item["id"]: item for item in all_items}
    selected = list(unique.values())[:12]
    documents, snippets = [], []
    for item in selected:
        fields, truncated = {}, list(item.get("truncated_fields", []))
        for field in TEXT_FIELDS:
            value = item["fields"].get(field)
            if field in item["unknown_fields"] or not isinstance(value, str):
                fields[field] = None
                continue
            limit = 300 if field == "title" else 1600
            fields[field] = value[:limit]
            if len(value) > limit and field not in truncated:
                truncated.append(field)
            for match in re.finditer(r"[^\n.!?]+[.!?]?", fields[field]):
                start, end = match.span()
                while start < end:
                    stop = min(start + 400, end)
                    quote = fields[field][start:stop]
                    if quote.strip() and len(snippets) < 96:
                        evidence_id = "s-" + hashlib.sha256(encode([item["id"], field, start, quote]).encode()).hexdigest()[:20]
                        snippets.append({"evidence_id": evidence_id, "item_id": item["id"],
                                         "field": field, "start": start, "quote": quote})
                    start = stop
        documents.append({"item_id": item["id"], "source_key": item["source_key"],
                          "fields": fields, "unknown_fields": item["unknown_fields"],
                          "truncated_fields": truncated})
    return {"as_of": source["as_of"], "target_item_id": focus["id"],
            "documents": documents, "relationships": relationships,
            "snippets": snippets,
            "coverage": {"scope": context.get("scope_coverage", "unknown"),
                         "dependencies": "unknown_snapshot_links_excluded",
                         "omitted_documents": len(unique) - len(selected),
                         "omitted_plans": context.get("omitted_plans", 0),
                         "snippet_limit": 96}}


def valid_evidence(citations, payload):
    if not isinstance(citations, list) or not citations:
        return False
    permitted = {s["evidence_id"]: s for s in payload["snippets"]}
    documents = {d["item_id"]: d for d in payload["documents"]}
    for citation in citations:
        if not isinstance(citation, dict) or citation.get("evidence_id") not in permitted:
            return False
        expected = permitted[citation["evidence_id"]]
        if citation != expected:
            return False
        doc = documents[expected["item_id"]]
        text = doc["fields"].get(expected["field"])
        if expected["field"] in doc["unknown_fields"] or not isinstance(text, str):
            return False
        start = expected["start"]
        if text[start:start + len(expected["quote"])] != expected["quote"]:
            return False
    return True
