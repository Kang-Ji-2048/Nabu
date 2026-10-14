"""Land source records and atomically replace normalized project snapshots."""

from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sqlite3
from uuid import uuid4

from .extract import QUERIES
from .classification import classify, VERSION as CLASSIFIER_VERSION


class InvalidRecord(ValueError):
    pass


def identifier(value) -> str:
    if isinstance(value, bool) or not str(value).isdigit() or int(value) < 1:
        raise InvalidRecord(f"Expected a positive source ID, got {value!r}")
    return str(int(value))


def required(row, key):
    value = row.get(key)
    if value is None or not str(value).strip():
        raise InvalidRecord(f"Missing {key}")
    return str(value)


def timestamp(value, *, mandatory=False):
    if value is None or value == "":
        if mandatory:
            raise InvalidRecord("Missing timestamp")
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError as exc:
        raise InvalidRecord(f"Invalid timestamp: {value!r}") from exc
    # TAWOS documents all its timezone-naive timestamps as UTC.
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def record_key(table, row):
    if table in {"Issue_Component", "Fix_Version", "Affected_Version"}:
        target = {"Issue_Component": "Component_ID", "Fix_Version": "Fix_Version_ID", "Affected_Version": "Affected_Version_ID"}[table]
        return identifier(row.get("Issue_ID")) + ":" + identifier(row.get(target))
    return identifier(row.get("ID"))


def event_kind(field):
    # TAWOS Change_Type is broader than a single field: STATUS includes
    # resolution, and STORY_POINT includes actual points recorded afterwards.
    return {
        "status": "status_changed", "resolution": "resolution_changed",
        "story points": "estimate_changed", "story point": "estimate_changed",
        "actual story points": "actual_estimate_changed",
        "summary": "text_changed", "description": "text_changed",
        "assignee": "people_changed", "reporter": "people_changed",
        "epic link": "membership_changed", "epic child": "membership_changed",
        "sprint": "membership_changed",
    }.get(field.casefold(), "field_changed")


def load(source_file: Path, database: Path, mapping_file: Path | None = None) -> dict:
    source_file = source_file.resolve()
    database = database.resolve()
    if source_file == database:
        raise ValueError("Source file and destination database must differ")
    mappings = json.loads((mapping_file or Path(__file__).with_name("mappings.json")).read_text(encoding="utf-8"))
    for category in ("statuses", "types", "link_descriptions"):
        if not isinstance(mappings.get(category), dict):
            raise ValueError(f"Mappings require an object named {category}")
    if not set(mappings["statuses"].values()) <= {"todo", "in_progress", "done", "cancelled"}:
        raise ValueError("Invalid canonical status in mapping")
    if not set(mappings["types"].values()) <= {"epic", "story", "task", "bug", "improvement"}:
        raise ValueError("Invalid canonical type in mapping")
    for value in mappings["link_descriptions"].values():
        if not isinstance(value, dict) or value.get("kind") not in {"blocks", "duplicates", "relates", "causes"} or type(value.get("reverse")) is not bool:
            raise ValueError("Invalid link mapping: expected kind and boolean reverse")
    digest = hashlib.sha256()
    with source_file.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    database.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database)
    connection.execute("PRAGMA foreign_keys=ON")
    connection.executescript(Path(__file__).with_name("schema.sql").read_text(encoding="utf-8"))
    source = "tawos-v1.1"
    run_id = str(uuid4())
    now = lambda: datetime.now(timezone.utc).isoformat()
    report = {"run_id": run_id, "source": source, "sha256": digest.hexdigest(),
              "raw": Counter(), "loaded": Counter(), "rejected": 0,
              "unmapped_statuses": Counter(), "unmapped_types": Counter(),
              "unmapped_links": Counter(), "external_links": 0, "snapshot_only": True,
              "work_categories": Counter(), "classifier_version": CLASSIFIER_VERSION}
    connection.execute("INSERT INTO ingestion_run VALUES (?,?,?,?,?,?,?,?)",
                       (run_id, source, str(source_file), digest.hexdigest(), now(), None, "running", None))
    connection.commit()

    def key(value):
        return source + ":" + identifier(value)

    def reject(line, table, source_id, reason, payload):
        report["rejected"] += 1
        connection.execute("INSERT INTO rejected_record VALUES (?,?,?,?,?,?)",
                           (run_id, line, table, source_id, str(reason), payload))

    def rows(table):
        cursor = connection.execute("SELECT source_id,payload FROM raw_record WHERE source=? AND table_name=? AND run_id=? ORDER BY source_id",
                                    (source, table, run_id))
        for source_id, payload in cursor:
            yield source_id, payload, json.loads(payload)

    try:
        connection.execute("BEGIN")
        connection.execute("CREATE TEMP TABLE source_line (table_name TEXT, source_id TEXT, line INTEGER, PRIMARY KEY(table_name,source_id))")
        with source_file.open(encoding="utf-8-sig") as stream:
            for line, content in enumerate(stream, 1):
                table = source_id = None
                try:
                    envelope = json.loads(content)
                    if not isinstance(envelope, dict):
                        raise InvalidRecord("Expected an object containing table and row")
                    table = envelope.get("table")
                    row = envelope.get("row")
                    if not isinstance(table, str) or table not in QUERIES or not isinstance(row, dict):
                        raise InvalidRecord("Unsupported table or missing row object")
                    source_id = record_key(table, row)
                    if connection.execute("SELECT 1 FROM source_line WHERE table_name=? AND source_id=?", (table, source_id)).fetchone():
                        raise InvalidRecord("Duplicate source ID in this export")
                    payload = json.dumps(row, ensure_ascii=False, sort_keys=True)
                    connection.execute("INSERT INTO source_line VALUES (?,?,?)", (table, source_id, line))
                    connection.execute("INSERT INTO raw_record VALUES (?,?,?,?,?) ON CONFLICT(source,table_name,source_id) DO UPDATE SET payload=excluded.payload,run_id=excluded.run_id",
                                       (source, table, source_id, payload, run_id))
                    report["raw"][table] += 1
                except (json.JSONDecodeError, InvalidRecord) as exc:
                    reject(line, table if isinstance(table, str) else None, source_id, exc, content)

        # Work with this export only. A project snapshot replaces previous entities;
        # rejected entities cannot leave stale normalized versions behind.
        project_ids = [key(source_id) for source_id, _, _ in rows("Project")]
        for project_id in project_ids:
            connection.execute("DELETE FROM event WHERE item_id IN (SELECT id FROM work_item WHERE project_id=?)", (project_id,))
            connection.execute("DELETE FROM link WHERE source_item_id IN (SELECT id FROM work_item WHERE project_id=?)", (project_id,))
            connection.execute("DELETE FROM work_item WHERE project_id=?", (project_id,))
            connection.execute("DELETE FROM project WHERE id=?", (project_id,))

        for table in ("Project", "Issue", "Change_Log", "Issue_Link"):
            for source_id, payload, row in rows(table):
                try:
                    if table == "Project":
                        connection.execute("INSERT INTO project VALUES (?,?,?,?,?)", (key(source_id), source, required(row, "Project_Key"), row.get("Name"), row.get("URL")))
                    elif table == "Issue":
                        project_id = key(row.get("Project_ID"))
                        if project_id not in project_ids:
                            raise InvalidRecord("Issue project is absent from this export")
                        estimate = row.get("Story_Point")
                        if estimate is not None:
                            try:
                                if isinstance(estimate, bool):
                                    raise ValueError()
                                estimate = float(estimate)
                                if not math.isfinite(estimate) or estimate < 0:
                                    raise ValueError()
                            except (ValueError, TypeError) as exc:
                                raise InvalidRecord("Invalid Story_Point; expected a nonnegative finite number") from exc
                        created = timestamp(row.get("Creation_Date"), mandatory=True)
                        resolved = timestamp(row.get("Resolution_Date"))
                        updated = timestamp(row.get("Last_Updated"))
                        if any(value and value < created for value in (resolved, updated)):
                            raise InvalidRecord("Resolution/update precedes creation")
                        status = row.get("Status") or ""
                        item_type = row.get("Type") or ""
                        if not isinstance(status, str) or not isinstance(item_type, str):
                            raise InvalidRecord("Status and Type must be strings or null")
                        status_category = mappings["statuses"].get(status.casefold(), "unknown")
                        canonical_type = mappings["types"].get(item_type.casefold(), "unknown")
                        title = required(row, "Title")
                        category = classify(title, row.get("Description"))
                        connection.execute("INSERT INTO work_item VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                           (key(source_id), project_id, source, required(row, "Issue_Key"), row.get("URL"),
                                            canonical_type, title, row.get("Description"), status, status_category,
                                            row.get("Resolution"), estimate, "points" if estimate is not None else None,
                                            str(row["Assignee_ID"]) if row.get("Assignee_ID") is not None else None,
                                            created, resolved, updated, 1))
                        connection.execute("INSERT INTO work_classification VALUES (?,?,?)",
                                           (key(source_id), category, CLASSIFIER_VERSION))
                        report["work_categories"][category] += 1
                        if status_category == "unknown":
                            report["unmapped_statuses"][status] += 1
                        if canonical_type == "unknown":
                            report["unmapped_types"][item_type] += 1
                    elif table == "Change_Log":
                        field = required(row, "Field")
                        kind = event_kind(field)
                        connection.execute("INSERT INTO event VALUES (?,?,?,?,?,?,?,?,?)", (key(source_id), key(row.get("Issue_ID")), timestamp(row.get("Creation_Date"), mandatory=True), kind, field,
                                           row.get("From_String"), row.get("To_String"), row.get("From_Value"), row.get("To_Value")))
                    else:
                        source_item = key(row.get("Issue_ID"))
                        origin = source_item
                        target = key(row.get("Target_Issue_ID"))
                        description = row.get("Description") or ""
                        if not isinstance(description, str):
                            raise InvalidRecord("Link Description must be a string or null")
                        mapping = mappings["link_descriptions"].get(description.casefold())
                        # Reverse only on explicit phrase semantics. Name/Direction
                        # alone do not establish whether a source blocks a target.
                        if mapping and mapping["reverse"]:
                            origin, target = target, origin
                        present = int(connection.execute("SELECT 1 FROM work_item WHERE id=?", (target,)).fetchone() is not None)
                        connection.execute("INSERT INTO link VALUES (?,?,?,?,?,?,?,?,?)", (key(source_id), source_item, origin, target, mapping["kind"] if mapping else "unknown", row.get("Direction"), description, present, 1))
                        origin_present = connection.execute("SELECT 1 FROM work_item WHERE id=?", (origin,)).fetchone() is not None
                        report["external_links"] += int(not present or not origin_present)
                        if not mapping:
                            report["unmapped_links"][description] += 1
                    report["loaded"][table] += 1
                except (InvalidRecord, sqlite3.IntegrityError) as exc:
                    line = connection.execute("SELECT line FROM source_line WHERE table_name=? AND source_id=?", (table, source_id)).fetchone()[0]
                    reject(line, table, source_id, exc, payload)
        if not report["loaded"]["Project"] or not report["loaded"]["Issue"]:
            raise ValueError("Export must contain at least one valid Project and Issue; previous data retained")
        # Refresh external-target markers when projects are loaded in separate runs.
        connection.execute("UPDATE link SET target_in_dataset=EXISTS(SELECT 1 FROM work_item w WHERE w.id=link.to_id)")
        report["status"] = "completed_with_rejections" if report["rejected"] else "completed"
        connection.execute("UPDATE ingestion_run SET completed_at=?,status=?,report=? WHERE id=?", (now(), report["status"], json.dumps(report), run_id))
        connection.commit()
    except Exception:
        connection.rollback()
        connection.execute("UPDATE ingestion_run SET completed_at=?,status=? WHERE id=?", (now(), "failed", run_id))
        connection.commit()
        raise
    finally:
        connection.close()
    return report
