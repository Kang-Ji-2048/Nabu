# Mac training workflow

The local environment `.venv-slm` uses MLX LM for Apple Silicon QLoRA. The selected base checkpoint is `Qwen/Qwen3-8B`; the original 4B instruction checkpoint and Qwen3-14B are also supported. For 8B/14B the training worker passes `enable_thinking=False` to the original template; the NVIDIA Unsloth training path is a separate alternative. MLX GPU execution must have access to Metal (the Codex filesystem sandbox may hide it).

Create the isolated Mac environment first:

```sh
python3 -m venv .venv-slm
.venv-slm/bin/python -m pip install -e '.[agents]' 'mlx-lm[train]==0.32.0' 'mlx==0.32.3' 'transformers==5.19.0'
```

ETL normalizes tickets, but tickets are not risk answers. Build historical plan/evidence examples, then add reviewed `Detection` targets. Do not train on current snapshots or label every later epic addition as a risk. Later outcomes remain separate from model input.

```sh
python -m nabu build-slm-dataset --database data/nabu.sqlite --cases data/training/case-specs.jsonl --output data/training/examples --train-before 2014-01-01 --eval-before 2015-01-01 --risk-types scope_gap dependency_gap validation_gap
```

Each case specification has `id`, `epic`, `as_of`, and optionally `group` for related epics. The builder reuses the production detector's exact evidence selection and payload. Add `target` (`risks`, `limitations`), `review_status: "approved"`, and `reviewer` to the specification after human review, then rebuild into a new directory. Two distinct exact prior-ticket citations and allowed risk types are validated. Drafts stay in `cases.jsonl`; only approved examples enter train/validation/test exports. Time partitions reject shared roots/members/groups across splits. Supply groups for duplicates not detectable from membership.

Training requires nonempty reviewed training and validation partitions. The script reconstructs messages, checks citation validity, checks related groups/time, preserves the original tokenizer chat template, and refuses examples exceeding the token budget.

```sh
.venv-slm/bin/python scripts/train-slm-mlx.py --checkpoint Qwen/Qwen3-8B --dataset data/training/examples --model-dir data/models/qwen3-8b-mlx-4bit --output data/training/run-1 --preflight-only
.venv-slm/bin/python scripts/train-slm-mlx.py --checkpoint Qwen/Qwen3-8B --dataset data/training/examples --model-dir data/models/qwen3-8b-mlx-4bit --output data/training/run-1
```

Defaults: 4-bit base, rank 16, batch 1, accumulation 8, learning rate 1e-4, one epoch, 8192-token context, prompt masking, gradient checkpointing, seed 3407. Iterations are rounded to a complete gradient accumulation group. The script records dependency versions and dataset hash. It requires `nabu-base.json` beside the converted model with `checkpoint` set to the exact base ID. A successful adapter run does not issue a production manifest.

Use MLX's conversion tool to create the 4-bit local base from the exact checkpoint. Record the source revision in `nabu-base.json`.

```sh
.venv-slm/bin/python scripts/prepare-slm-model.py --checkpoint Qwen/Qwen3-8B --output data/models/qwen3-8b-mlx-4bit
```

For deployment, fuse the adapter into dequantized weights with `mlx_lm.fuse --dequantize`, then convert Qwen to GGUF using llama.cpp's Hugging Face converter and quantizer. MLX's built-in GGUF exporter has model-family limitations; do not assume it supports Qwen. Import the resulting GGUF into Ollama with a Modelfile, verify chat template/context, and evaluate after quantization. Only then create the trained manifest with hashes of the real dataset and artifact.

The `evaluate-slm-baseline` command evaluates validation/test examples against the exact Ollama alias without a trained manifest and marks every report `untrained_baseline`. It records schema validity and citation-valid finding fraction; usefulness and false alarms require human review. Its byte guard is not tokenizer-aware context management.

```sh
python -m nabu evaluate-slm-baseline --dataset data/training/examples/validation.jsonl --output data/training/baseline.json --model YOUR_BASE_MODEL_ALIAS
```

Use an evaluation-only cases file; mixed training cases are rejected. This command is for base weights only.

References: [MLX LM training](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md), [Qwen checkpoint](https://huggingface.co/Qwen/Qwen3-8B).

To prepare the chronological holdout directly from the imported project:

```sh
.venv-slm/bin/python scripts/prepare-slm-cases.py --database data/nabu.sqlite --output data/training/xd-ticket-80-20 --risk-types scope_gap dependency_gap validation_gap
```

This reserves the latest 20% of tickets by creation time, then assigns historical epic plans to those time windows for test, with 10% of the earlier 80% of tickets set aside for validation. Plans are reviewed one day after epic creation. Split reports record exclusions for shared plan members, so inspect the final ratios. These are unlabelled drafts and cannot yet train the detector.

The local Spring XD ETL loaded 3,707 tickets and 43,227 events with zero rejections. The ticket split contains 2,965 development tickets (2,668 training plus 297 validation) and 742 test tickets. The corresponding historical plan drafts contain 86 training, 3 validation and 20 test examples. The test timeline starts at 2015-04-30T13:36:53Z. No approved labels exist yet; no detector training has run.

## Generate labels for review

```sh
.venv-slm/bin/python scripts/draft-slm-labels.py --dataset data/training/xd-ticket-80-20 --model-dir data/models/qwen3-8b-mlx-4bit --output data/training/xd-label-review
```

This uses the local base model to draft labels for training and validation only, validates the Detection schema, allowed risk types and exact historical citations, and writes `generated-labels.jsonl` plus a readable `review.md`. Machine labels remain `generated_unreviewed`. Citation checks do not establish whether a warning is useful. Failed labels are logged and omitted rather than converted to no-risk targets. Successful labels are checkpointed individually, so the command can resume.

After review, put approved/revised targets into the original case specifications with a named reviewer and rebuild the dataset using the recorded time boundaries. Training refuses unreviewed labels by default and refuses a dataset containing only risk or only no-risk targets. An explicit `--allow-generated-labels` option exists solely for user-authorized experiments; it records unreviewed provenance and does not issue a production manifest. The selected workflow requires human review before training.
