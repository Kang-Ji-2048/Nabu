# External project testing

Apache Mesos (`MESOS`) from the pinned TAWOS archive provides a separate project for testing a detector developed on Spring XD (`XD`). Use a separate SQLite database. Keep Mesos examples out of fine-tuning, prompt development and training-label generation.

The current portable package is `data/external-test/mesos-ai-reference-v1`: 32 frozen historical inputs and 32 Codex-reviewed AI reference targets, including 3 conditional validation suggestions. Run `.venv-slm/bin/python scripts/check-external-reference.py` without the source database. This explicit reference version retains the original fixed roster and records the v2 development-label hash; the original roster protocol is preserved as historical provenance. AI references are not independently adjudicated human ground truth and do not establish predictive accuracy. See [training-handoff.md](training-handoff.md) for the current preparation entry point.

```sh
.venv-slm/bin/python -m nabu extract-dump --input data/source/TAWOS.sql --project MESOS --output data/raw/mesos-external-test-v1.jsonl
.venv-slm/bin/python -m nabu load --input data/raw/mesos-external-test-v1.jsonl --database data/external-test/mesos-v1.sqlite --report data/reports/mesos-external-test-v1.json
.venv-slm/bin/python scripts/prepare-external-test.py --database data/external-test/mesos-v1.sqlite --project MESOS --development-labels data/training/xd-label-review/generated-labels.jsonl --output data/external-test/mesos-roster-v1
```

The roster selects up to 32 epics uniformly with fixed seed 3407 using only identity, epic type and creation-time metadata. Review cutoffs are one day after epic creation and at or after the latest development-label cutoff, including validation. This respects Nabu's declared training-cutoff constraint. The script checks that external ticket IDs do not overlap any supplied development plan or prior evidence IDs. It records the development-label hash and roster hash.

The roster is an evaluation protocol, not a labelled benchmark. No held-out ticket text, outcomes or model predictions are used to select examples. Complete these steps before drawing accuracy conclusions:

1. Freeze the model, detector prompt, retrieval policy and this roster. If development labels or taxonomy change, create an explicit new protocol version.
2. Reconstruct each test plan and prior evidence at its fixed cutoff. Report unknown fields, omitted scope and retrieval coverage. Do not use latest snapshots as model inputs.
3. Prepare reviewed reference risk labels with exact historical citations, blind to detector predictions. The current user-selected experimental package records AI generation/review explicitly. Independent adjudication is needed for stronger accuracy claims, rather than assumed from this package. Empty-risk targets mean no supported risks, not verified safety.
4. Run the frozen base and fine-tuned detectors, then the quantized deployment artifact, on identical inputs. Measure schema validity, citation validity, useful supported findings, false alarms and risk recall against reviewed references.
5. Report the observed positive-risk prevalence. Do not cherry-pick cases to guarantee positive examples. If references contain no positive risks, recall is undefined and additional testing is required under a new declared protocol.

Mesos is a different team/project with different terminology and status conventions. Inspect the ETL rejection/mapping report and historical evidence coverage before evaluation; topic similarity does not establish equivalent delivery risk.

The audited XD v2 exclusions/grouping proof remain required; external testing does not supply positive development-validation examples. It does not change the chosen training-label review provenance. Keep the original XD chronological holdout reserved.

To reproduce the frozen reference inputs from a separately imported Mesos database, use `scripts/prepare-external-reference.py` with the fixed roster and the exact development-label file, and choose a new output directory. The supplied package already includes the resulting inputs, so the training computer does not need to repeat extraction/import. Noncanonical source mappings remain explicit unknowns.

The base-only `evaluate-slm-baseline` command now accepts `external_test` inputs and `--checkpoint Qwen/Qwen3-8B`. This records the expected checkpoint; it does not verify an Ollama alias's weights. It measures format/citation validity and does not automatically score semantic agreement with these references. Frozen adapters and final quantized deployment weights require separate post-training evaluation. Do not run base-only evaluation against an adapter and report it as an untrained baseline.

The pinned tokenizer profile records a maximum external prompt of 12577 tokens. Use a serving context of at least 16384 and an explicit 2048 output-token budget; preserve the frozen evidence unchanged. This is a capacity setting based on inputs, not model-prediction-based tuning. For a separately verified untrained base alias, the existing base-only command can use `--max-input-bytes 128000 --max-tokens 2048 --checkpoint Qwen/Qwen3-8B`. Context configuration belongs to the serving runtime and is not set by this evaluation command. Long-context semantic quality remains unverified.
