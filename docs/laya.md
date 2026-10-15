# Local Laya risk labelling

Laya is the local annotation teacher. SLM training takes place on the separate
training machine. These commands do not train or replace that SLM.

The workspace has a separate `.venv-laya` with `laya==0.4.7` and CPU PyTorch.
On another Windows machine, from the repository root:

```powershell
uv venv .venv-laya --python 3.13
uv pip install --python .venv-laya/Scripts/python.exe --torch-backend cpu -r requirements/laya-tested.txt -e '.[laya]'
$env:PYTHONUTF8 = '1'
.venv-laya\Scripts\python.exe -m nabu prepare-laya
```

On Apple Silicon or Linux:

```bash
uv venv .venv-laya --python 3.13
uv pip install --python .venv-laya/bin/python -r requirements/laya-tested.txt -e '.[laya]'
.venv-laya/bin/python -m nabu prepare-laya
```

Use `.venv-laya/bin/python` for the remaining commands on those platforms. Start
with `--device cpu`; `--device auto` lets Laya select CUDA or Apple MPS when
available. Only the Windows CPU path has been exercised here; Mac/Linux execution
still needs confirmation on the destination machine. This environment is separate
from `.venv-slm` and does not start or change the existing training run.

Preparation downloads only `convaiinnovations/laya-typed-decisions`, pinned at
revision `1a793eb568e6718f15941d08f85432581df534e3`, into
`data/models/laya-typed-decisions`. It validates the CPU load and fingerprints the
normalized artifacts in `nabu-laya-manifest.json`. Matching interrupted downloads
can resume. No ticket data is involved in model download.

Inference loads the verified local directory, enables Hugging Face/Transformers
offline mode and disables Hugging Face telemetry. There is no hosted fallback.
For a strict data boundary, also block outbound networking for the inference
process at the operating-system/container level.

## Run

```powershell
.venv-laya\Scripts\python.exe -m nabu label-data --project XD --as-of 2013-10-01 --observed-through 2013-12-31 --output data/training/xd-2013-q4-v2
.venv-laya\Scripts\python.exe -m nabu classify-risks --provider laya --model data/models/laya-typed-decisions --device cpu --dataset data/training/xd-2013-q4-v2 --output data/training/xd-2013-q4-laya-v2 --limit 5
```

The dataset export needs a fresh directory. Rerun the classifier command to process
the next five unclassified tickets. Completed results are cached in SQLite. Input,
model fingerprint, device, rubric, threshold and provider settings are frozen;
changes require a new classifier output directory.

For a fresh-clone smoke test without downloading TAWOS, use the committed synthetic
fixture first (choose unused output directories):

```powershell
.venv-laya\Scripts\python.exe -m nabu load --input tests/fixtures/tawos-synthetic.jsonl --database data/laya-smoke/source.sqlite
.venv-laya\Scripts\python.exe -m nabu label-data --database data/laya-smoke/source.sqlite --project DEMO --as-of 2021-01-16 --observed-through 2021-02-01 --output data/laya-smoke/dataset
.venv-laya\Scripts\python.exe -m nabu classify-risks --provider laya --model data/models/laya-typed-decisions --dataset data/laya-smoke/dataset --output data/laya-smoke/predictions --limit 2
```

Synthetic output verifies plumbing only. The public Spring XD database is ignored
by Git: follow [etl.md](etl.md) to recreate it, or transfer your existing database
through your intended data channel. Weights and generated ticket datasets are
also ignored; the setup command fetches the pinned public model on the new machine.

The adapter supplies the focus ticket and at most two historical context documents.
It avoids sending duplicate snippet text with the documents. If Laya reports
truncated context or collapsed answer options, the ticket abstains. Omitted
documents, token usage and the actual provider-payload fingerprint are retained.

Above-threshold decisions undergo another local check against up to six exact
candidate excerpts per risk type. A deterministic rubric-word-overlap shortlist
bounds CPU work; it may miss evidence. Both positive and negative targets require
an accepted support decision, sufficient evidence confidence and exact substring
validation. Exact quotes prove provenance, not semantic correctness.

Confidence gating uses Laya's `answer_confidence`; normalized-entropy `confidence`
is retained as `entropy_confidence`. Neither is an evaluated probability of a
future delivery failure. The checkpoint has 1,024 tokens of context. Its runtime
warns about a clamped `choice:11+` calibration temperature; Nabu uses three-option
decision and support questions, so that bucket is not used. Three-option confidence
still needs validation on XD.

The first five-ticket local XD run completed with all decisions abstaining at
0.8, yielding zero training examples. This is a functioning pipeline, not evidence
that the pretrained checkpoint is ready to label our dataset accurately.

## Evaluation and handoff

```powershell
.venv-laya\Scripts\python.exe -m nabu sample-label-reference --dataset data/training/xd-2013-q4-v2 --predictions data/training/xd-2013-q4-laya-v2 --output data/training/xd-2013-q4-reference-v2 --size 100
```

The sample contains frozen inputs and empty targets, with teacher answers hidden.
After independent review, `evaluate-labels` measures per-type precision, recall
including missed positive abstentions, coverage and threshold sweeps. Unreviewed
templates cannot be scored as reference truth. Bulk annotation remains automatic.

Send the versioned data and manifests to the training machine. Mask null targets
in training; do not convert them to safe negatives. These ticket labels are auxiliary
supervision, not the full `assess` detector contract with actions and two historical
citations. See [the label specification](label-spec.md) and [workflow](labelling.md).

Jev and Claude remain optional hosted teachers. They can label public TAWOS examples;
future private tickets can stay local. Domain transfer must be evaluated. Hosted
teachers necessarily process supplied text; no-training/retention arrangements do
not mean the provider never sees it.

Primary references: [Laya source](https://github.com/NandhaKishorM/laya),
[checkpoint](https://huggingface.co/convaiinnovations/laya-typed-decisions).
