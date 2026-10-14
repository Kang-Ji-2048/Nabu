# Historical epoch 1 readiness (superseded)

This snapshot predates the user's selected Codex review. All 60 development labels have now received explicit AI review, with three text corrections, and the current export is `../xd-assistant-reviewed-v3`. The old pending human template below is retained as history. Use [the current M4 Pro 48GB handoff](../../../docs/training-handoff.md) and `../assistant-audit-v1/readiness.json` for the active preparation/launch path. AI review does not claim human approval.

## Earlier snapshot

Technical preparation is complete. Fine-tuning has not started. Human review of the version 2 labels is the remaining launch prerequisite.

The version 2 preparation audit explicitly proves the absent XD-3272/Jira64868 identity cannot enter imported development evidence; strict handling remains the default. Seventy unresolved-link children are quarantined. Original candidate and audit files are preserved.

The candidate package has 58 training examples (3 positive risk / 55 no supported risk) and 2 validation examples (both no supported risk). Complete sequences fit the 8,192-token budget, with a maximum of 6,547. Prefix checks verify assistant-only loss using Qwen's original template with thinking disabled. Runtime calibration on synthetic tokens passed at 6,667 tokens with 20.3 GB peak memory. The disposable adapter checkpoint saved/reloaded correctly and was discarded. No ticket labels were used for calibration.

Review `../xd-label-review-v2/review.md` and `../xd-label-review-v2/generated-labels.jsonl`. The decision template here has every case marked `pending` with a blank reviewer; no approval is assumed. Fill each selected decision with `approve`, `revise` or `reject` and the human reviewer's name. For `revise`, provide the complete corrected Detection target.

After direct human review:

```sh
cd /Users/phoebe/Nabu
.venv-slm/bin/python scripts/export-reviewed-slm.py --candidates data/training/xd-label-review-v2/generated-labels.jsonl --decisions data/training/epoch1-readiness/review-decisions.jsonl --preparation-manifest data/training/xd-development-v2/preparation-manifest.json --output data/training/xd-approved-v2
scripts/start-epoch1.sh data/training/xd-approved-v2 data/training/qwen3-8b-epoch1
```

The launcher runs preflight again and refuses unreviewed labels, stale/unaudited inputs, cross-partition IDs, invalid citations, empty/one-class training data, context overflow or a mismatched assistant prefix. It then requests exactly one sample pass, rank 16, batch 1, learning rate 1e-4, gradient checkpointing and seed 3407. Accumulation uses a divisor of the final sample count so the last gradients are applied without repeating examples: for all 58 approved examples, accumulation is 2 and there are 29 optimizer updates. Actual settings and hashes are recorded in the run.

Validation is too small and has no positive risk examples, so it can monitor loss but cannot measure risk recall. No positive scope-gap label exists. Mesos remains external testing, not training/validation. Final model-quality claims require independently reviewed external reference labels and evaluation after quantization.
