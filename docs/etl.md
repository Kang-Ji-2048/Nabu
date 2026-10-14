# TAWOS ETL

The initial pipeline is:

`TAWOS SQL dump (or MySQL) -> project JSONL export -> raw records -> canonical SQLite tables + run report`

Python 3.11+ is required. The local loader uses only the standard library. MySQL extraction requires the optional PyMySQL dependency. Run commands from the repository root.

## Try the local pipeline

```powershell
python -m nabu load --input tests/fixtures/tawos-synthetic.jsonl --database data/nabu.sqlite --report data/reports/synthetic.json
python -m unittest discover -s tests -v
```

The fixture is synthetic, not a sample of real Jira tickets. Repeating the load replaces the project's normalized snapshot without duplicating records. JSON progress/results go to stdout. Exit code 0 means completed; 2 means completed with quarantined records; 1 means failure. Rejections are stored in `rejected_record` with the original input and reason. On fatal failure, canonical/raw changes roll back and the run is marked failed.

## Load real data

### Direct dump reader (no database server required)

After extracting `TAWOS.sql.zip`, use the SQL file directly. Figshare's Download All option wraps the dataset ZIP inside another ZIP; extract both layers. The expanded SQL dump is 4,313,856,480 bytes.

```powershell
python -m nabu profile-dump --input data/source/TAWOS.sql --report data/reports/projects.json
python -m nabu extract-dump --input data/source/TAWOS.sql --project MESOS --output data/raw/mesos-v1.jsonl
python -m nabu load --input data/raw/mesos-v1.jsonl --database data/nabu.sqlite --report data/reports/mesos-v1.json
```

The reader parses the dump's column definitions and literal INSERT values without executing any SQL. It supports the single-line extended INSERT format in the published dump, including MySQL escaped strings, nulls and numeric literals. Unsupported expressions, missing column definitions and truncated INSERTs fail explicitly. It is not a general SQL interpreter. Extraction scans the dump three times and retains only the selected project's issue IDs in memory. Profile output compares issue, estimate, resolution, epic and sprint-membership coverage; it does not establish dependency/history completeness.

### Alternative: extract from a restored MySQL server

1. Review the upstream [TAWOS terms](https://github.com/SOLAR-group/TAWOS#terms-of-use). The authors state research-only use alongside an Apache 2.0 license. This pipeline supports research/evaluation; commercial dataset use needs separate clarification.
2. Download the pinned v1.1 archive using `./scripts/fetch-tawos.ps1`. Figshare lists a 637,550,449-byte ZIP; allow additional disk space for extraction and MySQL. The script verifies the upstream size and MD5 before publishing the archive filename. MD5 is used for download integrity, not authenticity.
3. Extract and restore the SQL dump into MySQL 8 following the [upstream installation instructions](https://github.com/SOLAR-group/TAWOS#installation-instructions). SQLite does **not** directly accept the MySQL dump as executable SQL. This dump's header names `tawos_cleaned`, but it does not necessarily create/select a database: restore into an explicitly selected database and set that name below. No MySQL server is bundled or started by Nabu.
4. Install the extraction dependency and configure credentials in the shell (see `.env.example`; no automatic dotenv loading):

```powershell
python -m pip install -e '.[mysql]'
$env:TAWOS_MYSQL_HOST = 'localhost'
$env:TAWOS_MYSQL_DATABASE = 'TAWOS'
$env:TAWOS_MYSQL_USER = 'root'
# Set TAWOS_MYSQL_PASSWORD in your shell if required; keep it out of source control.
python -m nabu extract --project MESOS --output data/raw/mesos-v1.jsonl
python -m nabu load --input data/raw/mesos-v1.jsonl --database data/nabu.sqlite --report data/reports/mesos-v1.json
```

MESOS is an example project key, not yet a validated demo choice. Extractor SQL uses bound parameters, a consistent read-only transaction and a streaming cursor. It exports only the selected project's issues and their related records. Files are written with a `.partial` suffix and renamed only when extraction succeeds. Existing exports are never overwritten; choose a new name for each snapshot. Failed partial exports are retained for investigation and must not be loaded.

## Data contract

Each JSONL line is `{"table":"Issue","row":{"ID":10,"Project_ID":1,...}}`, using the [upstream column names](https://github.com/SOLAR-group/TAWOS/blob/main/TAWOS_Database_Schema_Creation_Script.sql). Exported tables are Project, Issue, Change_Log, Issue_Link, Comment, Component, Issue_Component, Sprint, Version, Fix_Version and Affected_Version. Source database and table names are case sensitive on some MySQL installations.

| Layer | Stored data |
| --- | --- |
| `raw_record` | Latest accepted source row per table/ID, including unnormalized tables and derived outcome fields |
| `project` | Project key, name, URL and dataset-scoped identity |
| `work_item` | Ticket text, type, status, points, timestamps and source URL |
| `event` | Field-change timestamps plus original IDs and display values |
| `link` | Source ownership, normalized endpoint direction, relationship, external target marker |
| `ingestion_run` | Input path, SHA-256, time, status and quality report |
| `rejected_record` | Invalid rows with line numbers and reasons |

Keep immutable JSONL exports as the complete audit trail. `raw_record` is a latest-row landing table, not an archive of every historical import. Rows removed from later exports can remain in raw storage with their earlier `run_id`; normalization reads only rows belonging to the current run. SHA-256 fingerprints the input file, not a MySQL database version.

Loads are authoritative **complete project snapshots**. Do not feed a partial issue selection as an update: absent events, links and tickets for supplied projects are removed from normalized tables. At least one valid project and issue are required; an empty/invalid export cannot erase all existing data. Some malformed records can be quarantined while the remaining project loads, so callers must inspect exit code 2 and the rejection report. Loading another project preserves existing projects. Input order does not matter. Raw landing uses bounded per-row memory; each project is loaded in one transaction.

IDs are prefixed `tawos-v1.1:` to distinguish dataset surrogate IDs from Jira's live IDs. Events and links retain raw source fields. A link pointing outside the loaded projects is preserved; its endpoint may resolve after loading another project. Reciprocal source link records retain distinct IDs and must be deduplicated when counting dependencies.

Event kinds use explicit field names, rather than TAWOS's broad `Change_Type`: that category groups resolution with status, and actual story points with planned estimates. Actual points and resolution therefore have separate outcome event kinds. Epic/sprint membership changes are retained as membership events without claiming that full historical membership has been reconstructed.

## Mapping and historical correctness

`nabu/mappings.json` contains a conservative initial status/type/link mapping. Pass `--mappings path/to/project-mappings.json` to override it. Inspect the run's `unmapped_statuses`, `unmapped_types` and `unmapped_links`; unknown values stay `unknown`, rather than being guessed. Project-specific status semantics need review before relying on the normalized categories. A resolved status is not itself proof of successful delivery; `resolution` is kept separately.

The initial Spring XD import added `improvement` as an explicit canonical type, maps technical tasks to tasks, and treats `In PR` as work in progress. `A depends on B` normalizes to `B blocks A`; the reciprocal `is depended on by` phrase preserves the opposite orientation. Supersession links remain unknown rather than being interpreted as dependencies.

Only explicitly mapped relationship descriptions determine edge direction. For example, `A is blocked by B` becomes `B -> A`. Unmapped link semantics remain unknown. Parent/epic relations are not inferred from arbitrary links. Assignee IDs are anonymized source identities; projects are not assumed to be teams.

TAWOS timestamps are documented as UTC. The loader emits UTC ISO timestamps with uniform microsecond precision. Missing estimates remain null and zero points remain zero. Derived effort/duration values are retained in raw storage, not treated as original estimates or start timestamps.

**These tables are not direct historical model inputs.** `work_item` and `link` are explicitly marked `snapshot_only=1`. Filtering current snapshots by creation date still leaks later edits and outcomes. The separate [historical replay reader](replay.md) now reconstructs supported fields at an `as_of` cutoff and emits partial plans with unknown fields made explicit. Its audit and outcome artifacts are excluded from model inputs. Embeddings, feature generation, forecasting, Postgres loading and live Jira sync remain outside this slice.

## Validation status

The automated suite exercises dump literals and schema checks, project filtering, local normalization, replay, ordering, quarantine, unknown mappings, timestamps, estimates, rollback, snapshot replacement and external link direction. MySQL extraction tests use a mocked driver; a real MySQL extraction still needs a restored TAWOS instance. Docker Desktop failed locally during inference socket initialization, so the direct dump reader provides an independent route to the data.
