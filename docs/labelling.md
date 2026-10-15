# Automatic risk labelling

Nabu can create ticket-linked training data without manual review. It keeps two
sources of weak supervision separate: recorded history signals and Jev's judgement
of risk in cutoff-bound ticket text. Neither is ground truth.

For the TAWOS Spring XD setup, read the [v2 label specification](label-spec.md)
and [local Laya workflow](laya.md). Laya uses local assets. Jev and Claude are
optional hosted teachers; SLM training happens separately.

## Export history labels

From the repository root, with the project already imported:

```powershell
python -m nabu label-data --database data/nabu.sqlite --project XD --as-of 2014-01-01 --observed-through 2014-04-01 --output data/training/xd-2014-q1-weak-v1
```

Use a new output directory for each export. The example window is illustrative.
The export reads SQLite without modifying it and produces:

| File | Contents |
| --- | --- |
| `inputs.jsonl` | Stable example IDs and historically reconstructed ticket fields at `--as-of` |
| `labels.jsonl` | Matching example/ticket IDs, weak targets, observation window and source events |
| `manifest.json` | Rules, taxonomy, project-history profile, coverage and SHA-256 fingerprints |
| `split-relations.jsonl` | Snapshot relations used only for split grouping, excluded from features |

The observation window is **after** `--as-of` and **through** `--observed-through`,
inclusive at its upper bound. Tickets created after the cutoff and tickets with no
recoverable title or description are excluded. Unknown fields remain unknown.
Later snapshots never fill unknown historical text. Outcome events are isolated
in the label file and must not enter model features.

| Weak type | Recorded signal |
| --- | --- |
| `estimation` | A finite positive estimate increases; actual effort and initial zero-to-positive sizing are excluded |
| `rework` | Explicit reopening, or a completed status changes back to open/to do/in progress |
| `dependency` | Transition into blocked, on hold or impeded; the actual cause is unverified |

A matched target is `1`. Every other target is `null`, meaning unlabelled.
`no_observed_signal` is not a negative example: history may be incomplete or the
outcome may fall outside the window. This dataset supports positive-unlabelled
learning or auxiliary supervision; do not silently convert nulls into zeroes.

## Classify risks with Jev

Install the optional official TypeSafe SDK and set `TYPESAFE_API_KEY` in your shell.
`.env` files are not automatically loaded. Select a model ID available to your
account; see [TypeSafe's SDK documentation](https://docs.typesafe.ai/sdk/python).

```powershell
python -m pip install -e '.[jev]'
python -m nabu classify-risks --dataset data/training/xd-2014-q1-weak-v1 --output data/training/xd-2014-q1-jev-v1 --model jev --min-confidence 0.8 --limit 100
```

This command sends cutoff-bound title, description, acceptance criteria, observed
epic context, unknown-field names and cutoff to TypeSafe's hosted API. It never
sends future history labels. A decision request per ticket asks about `scope_gap`, `dependency`, `estimation`
and `rework`. Each returns `risk`, `no_risk`, or `insufficient_evidence`, with
confidence and a probability distribution. A `no_risk` choice requires explicit
resolution or inapplicability of that particular concern, rather than silence.
Insufficient evidence or confidence below the threshold produces a null target.
Otherwise risk maps to `1` and no-risk to `0`.

Another request selects supporting exact excerpts. Accepted positive and negative
targets require valid supplied evidence and sufficient evidence confidence. Shared
payloads are bounded to 12 documents and 96 snippets. Omissions and truncated
fields are explicit. Laya uses its narrower documented budget and local support checks.

The default confidence threshold of 0.8 is an initial operating choice and has not
been calibrated on Nabu data. These are teacher judgements about explicit concerns
in text, not measured probabilities of a later delivery failure. Status alone,
work topics and unknown fields are not sufficient grounds for a risk label.

The classifier output directory contains:

| File | Contents |
| --- | --- |
| `classifier.sqlite` | Frozen configuration and one committed result per completed ticket |
| `predictions.jsonl` | Ticket/example IDs, all decisions, probabilities, confidence, abstentions, requested and served model IDs |
| `training.jsonl` | Joined cutoff-bound `input` and `targets` for examples with at least one accepted teacher label |
| `manifest.json` | Input fingerprint, rubrics, thresholds, coverage counts and output fingerprints |

Train only on each row's `input`; use `targets` as supervision, masking null
targets in the loss. Predictions and history labels join via `example_id`.
Teacher-only `scope_gap` has no corresponding history rule. Disagreement between
teacher predictions and outcome proxies is retained rather than overwritten.

Rerun the same command to process the next batch or resume a failed call. `--limit`
bounds new tickets per invocation. Completed results are reused, including when
credentials are unavailable. Changing model, input bytes, rubrics or threshold
requires a new classifier output directory. Results commit per ticket; a crash
during an unfinished API call can repeat that call. Failed batches retain results
in SQLite; JSONL exports refresh after the next successful invocation.

## Training boundaries

The quality tooling keeps automatic annotation and evaluation separate:

```powershell
# Optional second hosted teacher, for data you intend to send to that provider.
python -m nabu classify-risks --provider claude --model <model-id> --dataset <dataset-dir> --output <second-teacher-dir>
python -m nabu combine-labels --dataset <dataset-dir> --predictions <first-teacher-dir> --predictions <second-teacher-dir> --output <consensus-dir>
python -m nabu sample-label-reference --dataset <dataset-dir> --predictions <first-teacher-dir> --output <reference-dir> --size 100
python -m nabu evaluate-labels --dataset <dataset-dir> --predictions <first-teacher-dir> --reference <reviewed-reference.jsonl> --output <evaluation-dir>
python -m nabu split-label-data --dataset <early-window-dir> --dataset <later-window-dir> --train-through 2013-12-31 --validation-through 2014-03-31 --output <splits-dir>
```

These angle-bracket values are placeholders; replace them before running. Consensus
requires accepted agreement from at least two distinct model identities and retains
disagreements/abstentions. Repeating the same model or served alias cannot manufacture
independent votes. Future outcomes remain separate auxiliary targets.

The reference template hides teacher decisions. Reviewers supply 0/1/null targets,
set `reviewed` to true and enter their reviewer identity. Evaluation refuses to
score untouched templates, and reports per-type precision, coverage, recall that
counts abstained positives as misses, and threshold sweeps. Stratified-sample
metrics are not population prevalence estimates.

The split builder respects observation-window ends and quarantines windows that
cross boundaries. Related tickets, repeated snapshots, matching normalized text
and matching long titles stay in one partition; earlier members reserved for a
later partition are quarantined. Snapshot links are grouping metadata only.
Reports include missing context, duplicate groups and sparse outcome-class warnings.
Join teacher/consensus training rows to `assignments.jsonl` using `example_id`; never
train on quarantined examples or use outcome files as cutoff-time risk ground truth.

This is a ticket classification dataset. It does not directly train the richer
`assess` detector contract, which also requires conditional claims, target plans,
actions and exact citations to two distinct historical tickets. Training that
detector still needs suitable plan-level examples and evaluation.

Keep repeated windows for the same ticket and related epic members together when
splitting training/evaluation data. Historical training availability is at least
the observation-window end, not just the input cutoff. Jev's base-model training
provenance is unknown, so its labels cannot certify a leakage-free historical
benchmark. Hold out reviewed data to assess classifier quality before relying on
these labels as evidence of model accuracy.

The initial local Spring XD export above produced 844 examples: 4 with a rework
signal and 840 without an observed rule signal; 312 tickets lacked recoverable
text and 2,551 were created after the cutoff. These counts describe coverage, not
risk prevalence. Live Jev quality has not been evaluated.
