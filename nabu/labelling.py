"""Automatic, ticket-linked outcome proxies with cutoff-bound input text."""

from collections import Counter
import hashlib
import json
import math
from pathlib import Path

from .pipeline import timestamp
from .replay import HistoricalReader, field_at
from .text import bounded_item


VERSION = "nabu.weak-labels.v2"
RISK_TYPES = ("estimation", "rework", "dependency")


def signals(event):
    """Conservative rules; a signal is an observation, not a causal diagnosis."""
    field = event["field"].strip().casefold()
    before = str(event["from_value"] or "").strip().casefold()
    after = str(event["to_value"] or "").strip().casefold()
    if field in {"story points", "story point"}:
        try:
            old = float(event["from_value"] if event["from_value"] is not None else event["from_id"])
            new = float(event["to_value"] if event["to_value"] is not None else event["to_id"])
        except (ValueError, TypeError):
            return []
        if math.isfinite(old) and math.isfinite(new) and 0 < old < new:
            return [("estimation", "estimate_increased")]
    if field == "status":
        if after == "reopened" and before and before != after:
            return [("rework", "explicit_reopening")]
        if before in {"done", "closed", "resolved"} and after in {"open", "to do", "in progress"}:
            return [("rework", "returned_from_done")]
        if after in {"blocked", "on hold", "impeded"} and before and before != after:
            return [("dependency", "blocked_status")]
    return []


def encode(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def historical_ticket(reader, item_id):
    item, _ = reader.item_at(item_id)
    # TAWOS has Acceptance Criteria change logs, but no canonical snapshot column.
    changes = [{**event, "field": "description"} for event in reader.events[item_id]
               if event["field"].casefold() == "acceptance criteria"]
    value, known, _ = field_at({**reader.items[item_id], "description": None, "updated_at": None},
                             changes, "description", reader.cutoff)
    item["fields"]["acceptance_criteria"] = value
    if not known:
        item["unknown_fields"].append("acceptance_criteria")
    item = bounded_item(item)
    if isinstance(value, str) and len(value) > 4000:
        item["fields"]["acceptance_criteria"] = value[:4000]
        item["truncated_fields"].append("acceptance_criteria")
    return item


def historical_contexts(reader):
    """Use observed Epic Child/Link histories, never current link snapshots."""
    roots = set()
    for item_id, events in reader.events.items():
        for event in events:
            if event["at"] > reader.cutoff:
                continue
            if event["field"].casefold() == "epic child":
                roots.add(item_id)
            if event["field"].casefold() == "epic link":
                for side in ("from", "to"):
                    key = reader.by_key.get(event[f"{side}_value"])
                    jira = reader.by_jira.get(str(event[f"{side}_id"]))
                    if key or jira:
                        roots.add(jira or key)
    contexts = {}
    for root_id in sorted(roots):
        if reader.items[root_id]["created_at"] > reader.cutoff:
            continue
        plan, _ = reader.plan(root_id)
        members = [item["id"] for item in plan["members"]]
        group = [root_id, *members]
        for item_id in group:
            contexts.setdefault(item_id, []).append((root_id, members))
    return contexts


def write_weak_labels(database: Path, project: str, cutoff: str, observed_through: str, output: Path):
    cutoff = timestamp(cutoff, mandatory=True)
    horizon = timestamp(observed_through, mandatory=True)
    if horizon <= cutoff:
        raise ValueError("--observed-through must be later than --as-of")
    output = output.resolve()
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError("Label output must be a new or empty directory")

    # Resolve the project without opening the source database for writes.
    import sqlite3
    from contextlib import closing
    with closing(sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)) as connection:
        projects = connection.execute("SELECT id FROM project WHERE source_key=?", (project,)).fetchall()
        if len(projects) != 1:
            raise ValueError(f"Expected one project for {project!r}; found {len(projects)}")
        root = connection.execute(
            "SELECT source_key FROM work_item WHERE project_id=? AND created_at<=? ORDER BY id LIMIT 1",
            (projects[0][0], cutoff)).fetchone()
    if root is None:
        raise ValueError("No project tickets existed at the cutoff")

    reader = HistoricalReader(database, root[0], cutoff)
    inputs, labels, relations = [], [], []
    counts = Counter()
    excluded = Counter()
    try:
        contexts = historical_contexts(reader)
        cache = {}
        def ticket_at(item_id):
            if item_id not in cache:
                cache[item_id] = historical_ticket(reader, item_id)
            return cache[item_id]
        # Snapshot relationships are grouping metadata only, excluded from features.
        for row in reader.connection.execute("SELECT from_id,to_id,kind FROM link WHERE source_item_id IN (SELECT id FROM work_item WHERE project_id=?)", (reader.root["project_id"],)):
            if row["from_id"] in reader.items and row["to_id"] in reader.items:
                relations.append({"item_ids": [row["from_id"], row["to_id"]], "kind": row["kind"], "grouping_only": True})
        for item_id, snapshot in sorted(reader.items.items()):
            if snapshot["created_at"] > cutoff:
                excluded["created_after_cutoff"] += 1
                continue
            item = ticket_at(item_id)
            if not any(str(item["fields"][name] or "").strip() for name in ("title", "description", "acceptance_criteria")):
                excluded["no_recoverable_text"] += 1
                continue
            example_id = hashlib.sha256(encode([VERSION, item_id, cutoff, horizon]).encode()).hexdigest()
            plans, group_ids = [], {item_id}
            for root_id, members in contexts.get(item_id, []):
                group_ids.update([root_id, *members])
                plans.append({"root": ticket_at(root_id), "members": [ticket_at(i) for i in members[:20]],
                              "omitted_members": max(0, len(members) - 20)})
            inputs.append({"example_id": example_id,
                           "input": {"as_of": cutoff, "ticket": item,
                                     "context": {"plans": plans[:3], "omitted_plans": max(0, len(plans) - 3),
                                                 "scope_coverage": "observed_membership_only",
                                                 "dependencies": "unknown_snapshot_links_excluded"}},
                           "group_item_ids": sorted(group_ids)})
            evidence = []
            for event in reader.events[item_id]:
                if not cutoff < event["at"] <= horizon:
                    continue
                for risk_type, rule in signals(event):
                    evidence.append({"risk_type": risk_type, "rule": rule,
                                     "event_id": event["id"], "item_id": item_id,
                                     "at": event["at"], "field": event["field"],
                                     "from_value": event["from_value"], "to_value": event["to_value"],
                                     "from_id": event["from_id"], "to_id": event["to_id"]})
            positive = sorted({e["risk_type"] for e in evidence})
            counts.update(positive)
            state = "observed_signal" if positive else "no_observed_signal"
            counts[state] += 1
            labels.append({"example_id": example_id, "item_id": item_id,
                           "source_key": item["source_key"], "project": project,
                           "label_kind": "weak", "reviewed": False, "state": state,
                           "target_definition": "later_recorded_outcome_proxy",
                           "targets": {risk: 1 if risk in positive else None for risk in RISK_TYPES},
                           "observation_window": {"after": cutoff, "through": horizon},
                           "evidence": evidence})
    finally:
        reader.close()
    if not inputs:
        raise ValueError("No tickets have recoverable text at the cutoff")

    contents = {"inputs.jsonl": "".join(encode(row) + "\n" for row in inputs),
                "labels.jsonl": "".join(encode(row) + "\n" for row in labels),
                "split-relations.jsonl": "".join(encode(row) + "\n" for row in relations)}
    hashes = {name: hashlib.sha256(body.encode("utf-8")).hexdigest() for name, body in contents.items()}
    manifest = {"version": VERSION, "project": project, "as_of": cutoff,
                "observed_through": horizon, "training_data_available_through": horizon,
                "risk_types": list(RISK_TYPES), "examples": len(inputs),
                "target_definition": "later_recorded_outcome_proxy",
                "profile": {"source": "TAWOS", "project": project,
                            "history_field_counts": dict(Counter(e["field"] for events in reader.events.values() for e in events)),
                            "status_transition_destinations": dict(Counter(e["to_value"] for events in reader.events.values() for e in events if e["field"].casefold() == "status")),
                            "tickets_with_plan_context": sum(bool(row["input"]["context"]["plans"]) for row in inputs)},
                "counts": dict(sorted(counts.items())), "excluded": dict(sorted(excluded.items())),
                "files": hashes,
                "dataset_sha256": hashlib.sha256(encode(hashes).encode()).hexdigest(),
                "target_semantics": "1 = observed proxy; null = unlabelled, never a confirmed negative",
                "rules": {"estimation": "Recorded story-point estimate increased.",
                          "rework": "Explicit reopening or return from a completed status.",
                          "dependency": "Transition into blocked, on hold or impeded; cause is unverified."},
                "limitations": ["Weak outcome proxies do not establish preventable risk or causality.",
                                "Missing events and right-censoring cannot establish negative labels.",
                                "Only inputs.jsonl input values may enter model features; labels contain future events.",
                                "Group repeated windows and related tickets before splitting for evaluation.",
                                "Ticket labels are auxiliary supervision, not the assessment detector output contract."]}
    output.mkdir(parents=True, exist_ok=True)
    for name, body in contents.items():
        with (output / name).open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(body)
    with (output / "manifest.json").open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    return {**manifest, "output": str(output)}
