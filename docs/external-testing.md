# External project testing

Apache Mesos (`MESOS`) from the pinned TAWOS archive provides a separate project for testing a detector developed on Spring XD (`XD`). Use a separate SQLite database. Keep Mesos examples out of fine-tuning, prompt development and training-label generation.

```sh
.venv-slm/bin/python -m nabu extract-dump --input data/source/TAWOS.sql --project MESOS --output data/raw/mesos-external-test-v1.jsonl
.venv-slm/bin/python -m nabu load --input data/raw/mesos-external-test-v1.jsonl --database data/external-test/mesos-v1.sqlite --report data/reports/mesos-external-test-v1.json
.venv-slm/bin/python scripts/prepare-external-test.py --database data/external-test/mesos-v1.sqlite --project MESOS --development-labels data/training/xd-label-review/generated-labels.jsonl --output data/external-test/mesos-roster-v1
```

The roster selects up to 32 epics uniformly with fixed seed 3407 using only identity, epic type and creation-time metadata. Review cutoffs are one day after epic creation and at or after the latest development-label cutoff, including validation. This respects Nabu's declared training-cutoff constraint. The script checks that external ticket IDs do not overlap any supplied development plan or prior evidence IDs. It records the development-label hash and roster hash.

The roster is an evaluation protocol, not a labelled benchmark. No held-out ticket text, outcomes or model predictions are used to select examples. Complete these steps before drawing accuracy conclusions:

1. Freeze the model, detector prompt, retrieval policy and this roster. If development labels or taxonomy change, create an explicit new protocol version.
2. Reconstruct each test plan and prior evidence at its fixed cutoff. Report unknown fields, omitted scope and retrieval coverage. Do not use latest snapshots as model inputs.
3. Obtain independently reviewed reference risk labels, with exact historical citations. Keep reference labelling blind to detector predictions. Empty-risk targets mean no supported risks, not verified safety.
4. Run the frozen base and fine-tuned detectors, then the quantized deployment artifact, on identical inputs. Measure schema validity, citation validity, useful supported findings, false alarms and risk recall against reviewed references.
5. Report the observed positive-risk prevalence. Do not cherry-pick cases to guarantee positive examples. If references contain no positive risks, recall is undefined and additional testing is required under a new declared protocol.

Mesos is a different team/project with different terminology and status conventions. Inspect the ETL rejection/mapping report and historical evidence coverage before evaluation; topic similarity does not establish equivalent delivery risk.

External testing does not repair the unresolved XD membership references and does not supply positive development-validation examples. It also does not replace human approval of training labels. Keep the original XD chronological holdout reserved; using it later requires the separate membership audit to be resolved.
