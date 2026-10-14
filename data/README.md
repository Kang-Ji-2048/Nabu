# Historical risk candidate data

`data/` is versionable; the repository no longer ignores the directory. This commit includes the frozen training/validation drafts, candidate targets, review records, ETL report and source provenance. The downloaded SQL dump/ZIP, local SQLite database, raw import and temporary labelling work remain local.

- `training/xd-ticket-80-20/`: 68 training and 2 validation drafts from the historical XD project, with split metadata and case specifications. No held-out test draft or test-ticket-ID file is published.
- `training/xd-label-review/`: 70 candidates, the readable review document, initial/final proposals, semantic review and provenance. There are 4 risk cases, 66 evidence-insufficient/no-risk cases and 0 label-validation failures. All labels are `generated_unreviewed`; none has human approval.
- `source/source-provenance.json` and `reports/xd-v1.json`: source checksums and import results. Source downloads can be obtained from the URL in the provenance file.

These are preserved outputs of the original preparation run, not a freshly regenerated dataset. The pre-publication membership audit found unresolved references in the imported source. The strengthened preparation code now quarantines tickets with unresolvable child Epic Links and stops on an unresolved held-out parent reference. See `training/xd-label-review/pre-publication-check.json` for the metadata-only findings and affected development cases. Existing inputs, cutoffs, fingerprints and labels were kept intact rather than silently replacing them.

The candidates pass Detection/citation validation, but require human semantic review and resolution of the grouping audit before training. There are only two validation cases, both without supported risks; this partition cannot measure risk recall or calibrate confidence. No model training or GPU labelling process was started.

Recorded absolute paths identify the original local run. When using these files from another checkout, resolve paths relative to this repository and verify the recorded hashes.

## Epoch-one preparation, version 2

The current review package is `training/xd-label-review-v2/`: 58 training candidates (3 positive risk / 55 no supported risk) and 2 no-risk validation candidates. All remain `generated_unreviewed`. The version 2 input preparation in `training/xd-development-v2/` records an explicit absence proof for the missing stable identity, quarantines unresolved-link children and preserves strict default behavior. Original version 1 inputs and labels above are unchanged.

`training/epoch1-readiness/` contains the launch plan, pending human-decision template and synthetic GPU calibration. The Mac completed a 6,667-token synthetic step at 20.3 GB peak memory and passed an adapter serialization roundtrip; that disposable adapter was discarded. No ticket-label fine-tuning has started. Human approval remains required.

`external-test/mesos-roster-v1/` contains a 32-case metadata roster for a separate Mesos external test, with source/import checks in `reports/mesos-external-test-v1.json`. It contains no test reference labels or model predictions. Downloaded data, model weights, runtime databases and locally reconstructed XD holdout inputs are ignored.
