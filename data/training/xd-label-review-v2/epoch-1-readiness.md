# Epoch 1 dataset readiness

The version 2 development dataset is prepared and all 60 targets are machine-labelled candidates ready for human review. There are 58 training examples (3 risk, 55 no-risk) and 2 validation examples (both no-risk). No fine-tuning has started, and no human approval or reviewer was invented.

Review `review.md`, especially positives XD-1260, XD-1317 and XD-1605. The old XD-1821 positive was rejected after its supporting XD-641 evidence was quarantined. Seventeen changed-evidence cases received fresh assistant assessment; 41 coverage-only changes were explicitly reassessed with unchanged supplied text; two full inputs match the original exactly. Original candidate/target/fingerprint artifacts remain frozen.

Preparation resolved the missing-reference blocker using an explicit, narrow `exclude-unimported` policy. XD-3272/Jira64868 has no matching imported or raw Issue identity. All 3,707 imported tickets have matching unique canonical key/Jira identities; the proof is recorded and hash-checked. No membership, missing child scope or outcome was invented. Preparation still fails by default on unresolved held-out references. The opt-in policy also fails closed for incomplete or inconsistent identity metadata, noncanonical IDs, label-only references and raw-only known identities. Seventy unresolved-link children remain quarantined; actual supplied input IDs do not intersect the manifest's excluded evidence IDs.

The chronological development/test boundaries are unchanged: 2,965 earlier tickets remain development locators and the latest 742 remain held out. Held-out cutoff plans were not reconstructed and no held-out text/outcomes were reviewed. New development historical evidence was reconstructed into `../xd-development-v2`, then labelled into this directory with source/target version provenance.

Every candidate passes Detection schema/exact citations and matches its preparation-manifest input hash. Complete chat sequences, including assistant targets, peak at 6,547 tokens, within 8,192. Non-thinking Qwen template prompt tokens exactly prefix the full sequence for every row, supporting assistant-only loss. Fourteen targeted preparation tests pass, including held-out exclusion and fail-closed identity checks.

Dataset preparation manifest: `../xd-development-v2/preparation-manifest.json`. Its `ready_for_training` flag certifies partition/evidence safety only. Approval remains separate: current `train.jsonl` and `validation.jsonl` contain `generated_unreviewed` rows and must not be supplied to actual fine-tuning until direct human review is recorded and approved exports are created in a new directory. The launcher must preserve the manifest input hashes on approval.

CPU preflight input:

```sh
cd /Users/phoebe/Nabu
.venv-slm/bin/python scripts/train-slm-mlx.py --checkpoint Qwen/Qwen3-8B --dataset data/training/xd-label-review-v2 --preparation-manifest data/training/xd-development-v2/preparation-manifest.json --model-dir data/models/qwen3-8b-mlx-4bit --output data/training/qwen3-8b-epoch-1 --preflight-only
```

After explicit human review, use the corresponding approved dataset directory for the actual epoch. Never use an unreviewed-label bypass for this workflow.

Evaluation limitation: two negative validation cases can report loss but cannot measure detector recall or calibrate risk confidence. Training positives are sparse and conditional. The model must be described as an initial experimental adapter until broader reviewed evaluation and deployment/quantization checks establish usefulness.
