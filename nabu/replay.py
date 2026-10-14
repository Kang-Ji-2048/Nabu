"""Conservative historical reads, with evaluation outcomes kept separately."""

from collections import defaultdict
import json
import math
from pathlib import Path
import sqlite3

from .pipeline import timestamp


# An allowlist prevents outcome/effort columns from entering model inputs.
FIELDS = {
    "title": ("title", {"summary"}),
    "description": ("description", {"description"}),
    "type": ("type", {"issuetype"}),
    "status": ("status", {"status"}),
    "estimate": ("estimate", {"story points", "story point"}),
}


def field_at(item, events, name, cutoff):
    column, aliases = FIELDS[name]
    changes = [event for event in events if event["field"].casefold() in aliases]
    before = [event for event in changes if event["at"] <= cutoff]
    after = [event for event in changes if event["at"] > cutoff]
    anchors = []
    if before:
        latest = max(event["at"] for event in before)
        anchors.extend((event["to_value"], event, "after_change") for event in before if event["at"] == latest)
    if after:
        earliest = min(event["at"] for event in after)
        anchors.extend((event["from_value"], event, "before_change") for event in after if event["at"] == earliest)
    evidence = [{"event_id": event["id"], "at": event["at"], "side": side} for _, event, side in anchors]
    if not anchors:
        # A later snapshot is never a default for an unobserved historical field.
        if item["updated_at"] is None or item["updated_at"] > cutoff:
            return None, False, {"reason": "no_temporal_evidence", "evidence": []}
        value = item[column]
        return value, True, {"reason": "snapshot_updated_by_cutoff", "evidence": []}
    candidates = []
    for value, event, side in anchors:
        raw_id = event["from_id" if side == "before_change" else "to_id"]
        if value is None and raw_id is not None:
            if name == "estimate":
                value = raw_id
            else:
                return None, False, {"reason": "missing_display_value", "evidence": evidence}
        candidates.append(value)
    if name == "estimate":
        try:
            candidates = [None if value in (None, "") else float(value) for value in candidates]
            if any(value is not None and (not math.isfinite(value) or value < 0) for value in candidates):
                raise ValueError()
        except (TypeError, ValueError):
            return None, False, {"reason": "invalid_historical_estimate", "evidence": evidence}
    if any(value != candidates[0] for value in candidates[1:]):
        # This includes same-time ambiguity and disagreement between old/new anchors.
        return None, False, {"reason": "conflicting_history", "evidence": evidence}
    return candidates[0], True, {"reason": "adjacent_change_evidence", "evidence": evidence}


class HistoricalReader:
    def __init__(self, database: Path, epic_key: str, cutoff: str):
        self.cutoff = timestamp(cutoff, mandatory=True)
        self.connection = sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)
        self.connection.row_factory = sqlite3.Row
        try:
            self.connection.execute("BEGIN")
            roots = self.connection.execute("SELECT * FROM work_item WHERE source_key=?", (epic_key,)).fetchall()
            if len(roots) != 1:
                raise ValueError(f"Expected one matching plan root for {epic_key!r}; found {len(roots)}")
            self.root = dict(roots[0])
            if self.root["created_at"] > self.cutoff:
                raise ValueError("Plan root did not exist at the cutoff")
            self.items = {row["id"]: dict(row) for row in self.connection.execute("SELECT * FROM work_item WHERE project_id=?", (self.root["project_id"],))}
            self.by_key = {item["source_key"]: iid for iid, item in self.items.items()}
            self.by_jira = {}
            for row in self.connection.execute("SELECT w.id,r.payload FROM raw_record r JOIN work_item w ON r.source=w.source AND r.source_id=substr(w.id,length(w.source)+2) WHERE r.table_name='Issue' AND w.project_id=?", (self.root["project_id"],)):
                jira_id = json.loads(row["payload"]).get("Jira_ID")
                if jira_id is not None:
                    self.by_jira[str(jira_id)] = row["id"]
            self.events = defaultdict(list)
            for row in self.connection.execute("SELECT e.* FROM event e JOIN work_item w ON w.id=e.item_id WHERE w.project_id=? ORDER BY e.at,e.id", (self.root["project_id"],)):
                self.events[row["item_id"]].append(dict(row))
        except Exception:
            self.connection.close()
            raise

    def close(self):
        self.connection.close()

    def item_at(self, item_id):
        item = self.items[item_id]
        if item["created_at"] > self.cutoff:
            raise ValueError("Item did not exist at the cutoff")
        values, audit, unknown = {}, {}, []
        for name in FIELDS:
            value, known, evidence = field_at(item, self.events[item_id], name, self.cutoff)
            values[name] = value
            audit[name] = evidence
            if not known:
                unknown.append(name)
        return {"id": item_id, "source_key": item["source_key"], "created_at": item["created_at"],
                "fields": values, "unknown_fields": unknown}, audit

    def membership_changes(self, root_id=None):
        """Combine parent Epic Child and child Epic Link observations."""
        changes = defaultdict(list)
        unresolved = []
        root = self.items[root_id or self.root["id"]]

        def reference(label, jira_id):
            by_key = self.by_key.get(label)
            by_jira = self.by_jira.get(str(jira_id)) if jira_id is not None else None
            if by_key and by_jira and by_key != by_jira:
                return None
            return by_jira or by_key

        for event in self.events[root["id"]]:
            if event["field"].casefold() != "epic child":
                continue
            for column, member in (("from_value", False), ("to_value", True)):
                child_key = event[column]
                jira_id = event["from_id" if column == "from_value" else "to_id"]
                if not child_key and jira_id is None:
                    continue
                child_id = reference(child_key, jira_id)
                if child_id:
                    changes[child_id].append((event, member))
                else:
                    unresolved.append({"event_id": event["id"], "at": event["at"], "child_key": child_key, "jira_id": jira_id})
        for item_id, events in self.events.items():
            if item_id == root["id"]:
                continue
            for event in events:
                if event["field"].casefold() != "epic link":
                    continue
                if reference(event["from_value"], event["from_id"]) == root["id"]:
                    changes[item_id].append((event, False))
                if reference(event["to_value"], event["to_id"]) == root["id"]:
                    changes[item_id].append((event, True))
        return changes, unresolved

    def plan(self, root_id=None):
        root_id = root_id or self.root["id"]
        root, root_audit = self.item_at(root_id)
        changes, unresolved = self.membership_changes(root_id)
        members, member_audits, membership_audit = [], {}, []
        for item_id, observations in changes.items():
            eligible = [(event, member) for event, member in observations if event["at"] <= self.cutoff]
            if not eligible:
                continue
            at = max(event["at"] for event, _ in eligible)
            latest = [(event, member) for event, member in eligible if event["at"] == at]
            states = {member for _, member in latest}
            issue = None
            if len(states) != 1:
                issue = "conflicting_membership_at_same_time"
            elif self.items[item_id]["created_at"] > self.cutoff:
                issue = "membership_precedes_item_creation"
            membership_audit.append({"item_id": item_id, "at": at, "event_ids": sorted({event["id"] for event, _ in latest}), "issue": issue})
            if issue or states != {True}:
                continue
            item, audit = self.item_at(item_id)
            members.append(item)
            member_audits[item_id] = audit
        members.sort(key=lambda item: item["source_key"])
        plan = {
            "format": "nabu.historical-plan.v1", "as_of": self.cutoff,
            "policy": "evidence_only", "scope_coverage": "observed_membership_only",
            "root": root, "members": members,
            "dependencies": {"status": "unknown", "reason": "Current link snapshots have no reliable creation timestamps."},
            "comments": {"status": "excluded", "reason": "Comment creation dates do not establish when their current text was written."},
        }
        audit = {"not_model_input": True, "as_of": self.cutoff, "root_fields": root_audit, "member_fields": member_audits,
                 "membership_evidence": membership_audit,
                 "unresolved_membership_references": [event for event in unresolved if event["at"] <= self.cutoff],
                 "assumptions": ["Recorded field values persist between logged changes.",
                                 "Missing change-log entries cannot be detected in every case.",
                                 "Source issue keys and creation times are used as dataset locators."]}
        return plan, audit

    def reveal(self, plan):
        """Evaluation only: this object must not be passed to review agents."""
        changes, _ = self.membership_changes()
        initial = {item["id"] for item in plan["members"]}
        additions = {}
        for item_id, observations in changes.items():
            if item_id in initial:
                continue
            later = [event["at"] for event, member in observations if member and event["at"] > self.cutoff]
            if later:
                additions[item_id] = min(later)
        return {"evaluation_only": True, "as_of": self.cutoff,
                "root_outcome": {name: self.root[name] for name in ("source_key", "title", "status", "resolution", "resolved_at")},
                "initial_member_outcomes": [{name: self.items[item["id"]][name] for name in ("source_key", "status", "resolution", "resolved_at")} for item in plan["members"]],
                "later_observed_additions": [{"source_key": self.items[item_id]["source_key"], "added_at": at,
                    "relative_to_recorded_resolution": "unresolved" if self.root["resolved_at"] is None else "before_or_at_resolution" if at <= self.root["resolved_at"] else "after_resolution"}
                    for item_id, at in sorted(additions.items(), key=lambda pair: pair[1])],
                "note": "Later additions are scope observations, not proof of delay or a missed deadline."}


def write_replay(database: Path, epic_key: str, cutoff: str, output: Path):
    names = ("plan.json", "audit.json", "outcome.json")
    if any((output / name).exists() for name in names):
        raise ValueError("Replay output already exists; choose a new output directory")
    reader = HistoricalReader(database, epic_key, cutoff)
    try:
        plan, audit = reader.plan()
        outcome = reader.reveal(plan)
    finally:
        reader.close()
    output.mkdir(parents=True, exist_ok=True)
    for name, value in zip(names, (plan, audit, outcome)):
        (output / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"root": epic_key, "as_of": plan["as_of"], "members": len(plan["members"]),
            "unknown_root_fields": plan["root"]["unknown_fields"],
            "outputs": [str(output / name) for name in names]}
