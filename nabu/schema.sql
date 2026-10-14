PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS schema_version (version INTEGER PRIMARY KEY);
INSERT OR IGNORE INTO schema_version VALUES (1);
CREATE TABLE IF NOT EXISTS ingestion_run (
    id TEXT PRIMARY KEY, source TEXT NOT NULL, source_file TEXT NOT NULL,
    sha256 TEXT NOT NULL, started_at TEXT NOT NULL, completed_at TEXT,
    status TEXT NOT NULL, report TEXT
);
CREATE TABLE IF NOT EXISTS raw_record (
    source TEXT NOT NULL, table_name TEXT NOT NULL, source_id TEXT NOT NULL,
    payload TEXT NOT NULL, run_id TEXT NOT NULL REFERENCES ingestion_run(id),
    PRIMARY KEY (source, table_name, source_id)
);
CREATE TABLE IF NOT EXISTS project (
    id TEXT PRIMARY KEY, source TEXT NOT NULL, source_key TEXT NOT NULL,
    name TEXT, url TEXT
);
CREATE TABLE IF NOT EXISTS work_item (
    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
    source TEXT NOT NULL, source_key TEXT NOT NULL, url TEXT,
    type TEXT NOT NULL, title TEXT NOT NULL, description TEXT,
    status TEXT, status_category TEXT NOT NULL, resolution TEXT,
    estimate REAL, estimate_unit TEXT, assignee TEXT,
    created_at TEXT NOT NULL, resolved_at TEXT, updated_at TEXT,
    snapshot_only INTEGER NOT NULL DEFAULT 1 CHECK (snapshot_only = 1)
);
CREATE INDEX IF NOT EXISTS work_item_project ON work_item(project_id);
CREATE TABLE IF NOT EXISTS event (
    id TEXT PRIMARY KEY, item_id TEXT NOT NULL REFERENCES work_item(id),
    at TEXT NOT NULL, kind TEXT NOT NULL, field TEXT NOT NULL,
    from_value TEXT, to_value TEXT, from_id TEXT, to_id TEXT
);
CREATE INDEX IF NOT EXISTS event_item_at ON event(item_id, at);
CREATE TABLE IF NOT EXISTS link (
    id TEXT PRIMARY KEY, source_item_id TEXT NOT NULL REFERENCES work_item(id),
    from_id TEXT NOT NULL,
    to_id TEXT NOT NULL, kind TEXT NOT NULL, source_direction TEXT,
    description TEXT, target_in_dataset INTEGER NOT NULL,
    snapshot_only INTEGER NOT NULL DEFAULT 1 CHECK (snapshot_only = 1)
);
CREATE TABLE IF NOT EXISTS rejected_record (
    run_id TEXT NOT NULL REFERENCES ingestion_run(id), line_number INTEGER NOT NULL,
    table_name TEXT, source_id TEXT, reason TEXT NOT NULL, payload TEXT NOT NULL,
    PRIMARY KEY (run_id, line_number)
);
