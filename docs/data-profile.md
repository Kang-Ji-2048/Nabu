# Initial TAWOS inspection

The downloaded Figshare bundle (`data/21308124.zip`) contained `TAWOS.sql.zip`.
The inner archive matched the upstream MD5 `e9c5ecc7649d55f0cf2fb4efb5664494`.
The extracted SQL dump is 4,313,856,480 bytes.

Nabu's direct dump reader counted **458,232 issues across 39 projects**, matching
the published v1.1 issue count. Full local results are in
`data/reports/projects.json` (ignored by Git).

| Candidate | Issues | With estimates | Epics | With sprint membership |
| --- | ---: | ---: | ---: | ---: |
| Spring XD (`XD`) | 3,707 | 3,705 | 109 | 2,156 |
| LSST Data Management (`DM`) | 26,506 | 20,664 | 2,407 | 8,684 |
| Apache Mesos (`MESOS`) | 10,157 | 3,272 | 282 | 2,887 |

Spring XD is the first import candidate because it is small enough to inspect
and has estimates on almost every ticket. This is not yet a finding that its
forecasts will be accurate. Estimate values, temporal history, dependency
semantics and recoverable epic membership need inspection before the backtest.

The original MySQL route remains supported. On this machine Docker Desktop
failed during inference socket initialization, so the SQL dump reader avoids
that dependency without executing the dump's SQL.

## Spring XD import result

The first real project was exported to `data/raw/xd-v1.jsonl` and loaded into
`data/nabu.sqlite`. The final run report is `data/reports/xd-v1.json`.

- 3,707 work items and 43,227 change events.
- 940 source link records, including reciprocal records of the same relationship.
- 4,120 comments, 66 sprints, 37 versions and 18 components preserved as raw data.
- Zero rejected records; no unmapped statuses or issue types after refining mappings.
- 36 supersession links retain unknown canonical semantics; source text is preserved.

Database integrity and foreign key checks passed. The normalized database contains
only the real XD project, with no synthetic demo items. A repeat load after mapping
refinement replaced the snapshot successfully. The automated suite has 17 passing
tests, including direct dump parsing, outcome separation and dependency direction.

History includes 610 planned-estimate changes, 541 actual-estimate changes and
9,470 membership events. The presence of those events supports further exploration,
but does not itself prove that every past field or epic membership is recoverable.
