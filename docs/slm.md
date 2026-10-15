# SLM risk detection and Claude reporting

For a separate local ticket-labelling teacher, see [Laya](laya.md). Its weak ticket
labels are auxiliary supervision, not replacements for the reviewed plan-level
targets used by the training workflow below.

The new `assess` command implements the SLM-to-Claude architecture. The existing
`review` command remains the LangGraph investigator/critic baseline. `assess`
does not use Claude to detect risks or silently substitute another detector.

## Implementation status

Ingestion normalises fields, assigns a deterministic work topic, and stores both
in SQLite. The versioned `work_classification` table records topic assignments;
the ingestion report includes counts. These rule-based topics are separate from
the existing optional embedding/HDBSCAN category discovery and from SLM risk
labels. Re-run `load` to populate classifications in an older database.

Assessment freezes the historical plan and eligible prior text, retrieves a
bounded lexical evidence sample, calls a locally served trained SLM, validates
its proposed citations, and passes supported candidates to Claude. Claude
produces concise explanations and actions. Python renders a Markdown report
alongside structured JSON. The evidence supplied to the SLM includes counterexample
candidates, not only historically completed work. It is a lexical sample, not a
complete review of every eligible ticket.

The local dataset builder and Apple Silicon training script are documented in
[slm-training.md](slm-training.md). Reviewed risk targets are required; the current user-selected AI-reviewed experimental package and Mac preparation are described in [training-handoff.md](training-handoff.md). No trained risk model is bundled or claimed to exist. Live detection and
report quality have not been evaluated. Offline mode tests wiring only.

## Try without model services

Install the existing agent extra and import data first:

```powershell
python -m pip install -e '.[agents]'
python -m nabu load --input tests/fixtures/tawos-synthetic.jsonl --database data/slm-demo/source.sqlite
```

For an imported Spring XD dataset, use a fresh run directory:

```powershell
python -m nabu assess --database data/nabu.sqlite --epic XD-238 --as-of '2013-06-17T23:59:59.999999Z' --run-dir data/assessments/xd-offline --offline --pause-after-prepare
python -m nabu assess --run-dir data/assessments/xd-offline --resume
```

The synthetic fixture has different epic keys; the XD command requires the real
import described in [etl.md](etl.md). Offline output has
`analysis_performed: false` and no findings. It does not certify plan safety.

## Training handoff

The model owner should supply:

1. A trained/fine-tuned small language model for evidence-grounded delivery-risk
   detection, with a documented label taxonomy and held-out evaluation.
2. A server exposing `/v1/chat/completions`, accepting schema-constrained JSON
   completions and returning the served alias as `model`. The adapter follows
   the [llama.cpp server API](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).
3. A provenance manifest based on [slm-manifest.example.json](slm-manifest.example.json).
   Replace the hashes, cutoff and taxonomy with actual values, and set `trained`
   to `true` only after training. The example is intentionally rejected by live
   assessment while `trained` is `false`.

The training-data cutoff must be at or before the historical review cutoff.
Otherwise Nabu refuses the model, since later outcomes would contaminate a
historical evaluation. The manifest is an operator declaration: hashes identify
the supplied artifact/dataset but the HTTP adapter cannot independently verify
the served weights or undocumented base-model training data. A declared cutoff
also does not prove that the target plan was held out.

The exact detector output contract is available without an API call:

```powershell
python -m nabu slm-schema --output data/training/detection-schema.json
```

The detector sees a JSON object containing `plan`, `prior_work`,
`allowed_risk_types`, and `coverage`. Every ticket has known historical fields,
unknown/truncated-field lists, an ID and a source key. Each proposed risk must
include an allowed `risk_type`, conditional claim, rationale, suggested action,
severity, target plan IDs and exact title/description citations from at least two
distinct supplied prior tickets. Return an empty risk list when unsupported.
The result is `{ "risks": [...], "limitations": [...] }`.

The default evidence limit is 12, configurable from 2 to 20. Up to 20 plan
members are supplied. Detector titles/descriptions are bounded to 200/1,200
characters; truncation and omitted-member counts are explicit. Historical
categories are recomputed from this text, never read from a later snapshot.
Audit files and later outcome artifacts do not enter model input.

## Live assessment once the trained model is available

Serve the trained model locally with alias matching the manifest's `model`
(for example, `llama-server -m <trained-model.gguf> --alias nabu-risk-slm
--host 127.0.0.1 --port 8080`). Set `ANTHROPIC_API_KEY` and `NABU_MODEL` in your
shell, then:

```powershell
python -m nabu assess --database data/nabu.sqlite --epic XD-238 --as-of '2013-06-17T23:59:59.999999Z' --manifest data/models/risk/manifest.json --slm-endpoint http://127.0.0.1:8080/v1 --run-dir data/assessments/xd-live
```

The adapter permits loopback endpoints only, disables proxies and redirects,
requires a matching model alias, and rejects incomplete/non-JSON completions.
Claude receives only citation-validated candidates; it cannot add risk IDs or
omit/duplicate candidates in its structured presentation. Exact citations,
severity and risk types are rendered from the SLM output, not Claude-generated
text. Valid citations establish provenance, not causal validity or comparability.
Claude's prose still requires human review.

## Recovery and outputs

Each completed run contains:

| File | Contents |
| --- | --- |
| `assessment.sqlite` | Frozen model input, manifest, stage results and resume position |
| `review.json` | Validated potential risks, rejected citations, presentation, coverage and provenance |
| `review.md` | Readable review with exact historical quotes and suggested actions |
| `events.json` | Completed, skipped and failed stages |

Use `--resume` with the same run directory after fixing a service failure. A
failed Claude call resumes from presentation without repeating completed SLM
detection. Saved stage inputs remain frozen even if the source store changes.
Model/manifest, cutoff, source locator, endpoint and evidence limits cannot be
changed on resume. Reading a completed assessment makes no model calls.

The checkpoint is a local sequential workflow, not a distributed job scheduler.
A crash during a model request may require repeating that unfinished request;
only successfully saved stages are skipped.
