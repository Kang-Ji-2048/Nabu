"""Train Nabu's reviewed detector examples on Apple Silicon with MLX QLoRA."""
import argparse
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import subprocess
import sys

# Allow running directly from a source checkout.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.slm import CHECKPOINT, SUPPORTED_CHECKPOINTS, messages
from nabu.risk.runner import validate_detection
from nabu.pipeline import timestamp


def read_partition(path, split, allow_generated=False, inspect_only=False):
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    if not rows:
        raise ValueError(f"{split} partition is empty")
    seen = set()
    for row in rows:
        if row['id'] in seen:
            raise ValueError('Duplicate example IDs in a training partition')
        seen.add(row['id'])
        reviewed = row.get("review_status") == "approved" and isinstance(row.get("reviewer"), str) and row["reviewer"].strip()
        generated = (allow_generated or inspect_only) and row.get("review_status") == "generated_unreviewed" and row.get("label_source", {}).get("kind") in {"local_model", "assistant_generated", "evidence_rule"}
        if row.get("split") != split or not (reviewed or generated):
            raise ValueError("Training requires approved, named human reviews in the correct split")
        checked = validate_detection(row["target"], row["input"])
        if checked["rejected"]:
            raise ValueError(f"Invalid training citations: {row['id']}")
        # Reconstruct messages to avoid accepting manually edited hidden outcome text.
        row["messages"] = messages(row["input"]) + [{"role": "assistant", "content": json.dumps(row["target"], ensure_ascii=False)}]
    return rows


def validate_preparation(path, rows):
    if path is None:
        raise ValueError('Training requires --preparation-manifest from an audited dataset version')
    manifest = json.loads(path.read_text())
    if manifest.get('version') != 'nabu-training-preparation-v1' or manifest.get('ready_for_training') is not True:
        raise ValueError('Dataset preparation audit is not ready for training')
    inputs = manifest.get('inputs', {})
    for row in rows:
        digest = hashlib.sha256(json.dumps(row['input'], sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()
        if inputs.get(row['id']) != digest:
            raise ValueError(f"Dataset input is absent from or differs from preparation audit: {row['id']}")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", choices=SUPPORTED_CHECKPOINTS, default=CHECKPOINT)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--model-dir", type=Path, required=True, help="4-bit MLX conversion of the exact Qwen checkpoint")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--epochs", type=float, default=1)
    parser.add_argument("--max-seq-length", type=int, default=8192)
    parser.add_argument("--learning-rate", type=float, default=1e-4)
    parser.add_argument("--gradient-accumulation", type=int, default=8)
    parser.add_argument("--allow-generated-labels", action="store_true", help="Experimental run on unreviewed machine labels; no production model claim")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--preparation-manifest", type=Path, help="Versioned partition/evidence audit; required to train")
    args = parser.parse_args()
    if args.epochs <= 0 or args.max_seq_length < 1 or args.gradient_accumulation < 1 or args.learning_rate <= 0:
        raise ValueError("Training settings must be positive")
    train = read_partition(args.dataset / "train.jsonl", "train", args.allow_generated_labels, args.preflight_only)
    valid = read_partition(args.dataset / "validation.jsonl", "validation", args.allow_generated_labels, args.preflight_only)
    if {row['id'] for row in train} & {row['id'] for row in valid}:
        raise ValueError('Example IDs overlap training and validation')
    preparation = validate_preparation(args.preparation_manifest, train + valid) if args.preparation_manifest else None
    if not args.preflight_only and preparation is None:
        raise ValueError('Training requires --preparation-manifest from an audited dataset version')
    if not any(row["target"]["risks"] for row in train) or not any(not row["target"]["risks"] for row in train):
        raise ValueError("Training needs both supported-risk and no-risk targets; refusing a degenerate label set")
    def groups(rows):
        return {value for row in rows for value in [row["group"], row["epic"], *(item["id"] for item in [row["input"]["plan"]["root"], *row["input"]["plan"]["members"]])]}
    if groups(train) & groups(valid):
        raise ValueError("Training and validation contain related plans")
    if max(timestamp(row["as_of"], mandatory=True) for row in train) >= min(timestamp(row["as_of"], mandatory=True) for row in valid):
        raise ValueError("Validation must follow training in time")
    # All supported checkpoints use Qwen's original template. Disable thinking
    # explicitly for 8B/14B; the worker passes the same switch during training.
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
    if not tokenizer.chat_template:
        raise ValueError("Original Qwen chat template is missing")
    lengths = []
    for row in train + valid:
        full = tokenizer.apply_chat_template(row['messages'], tokenize=True, return_dict=False, enable_thinking=False)
        prompt = tokenizer.apply_chat_template(row['messages'][:-1], tokenize=True, return_dict=False, enable_thinking=False, add_generation_prompt=True)
        if not prompt or len(prompt) >= len(full) or full[:len(prompt)] != prompt:
            raise ValueError(f"Assistant-only loss prefix does not match: {row['id']}")
        lengths.append(len(full))
    if max(lengths) > args.max_seq_length:
        raise ValueError(f"Example has {max(lengths)} tokens; exceeds context. Rebuild evidence or raise max-seq-length; no silent truncation.")
    config = json.loads((args.model_dir / "config.json").read_text())
    quantization = config.get("quantization", config.get("quantization_config", {}))
    if quantization.get("bits") != 4:
        raise ValueError("Model must be an MLX 4-bit conversion")
    # Require conversion provenance, not just a directory name.
    provenance = json.loads((args.model_dir / "nabu-base.json").read_text())
    if provenance["checkpoint"] != args.checkpoint:
        raise ValueError("Wrong base checkpoint")
    reviewed = all(row.get('review_status') == 'approved' for row in train + valid)
    iterations = math.ceil(len(train) * args.epochs)
    # MLX updates only on complete accumulation groups. Use a divisor of the
    # actual iteration count instead of repeating examples or losing the tail.
    accumulation = math.gcd(iterations, args.gradient_accumulation)
    print(json.dumps({"train": len(train), "validation": len(valid), "max_tokens": max(lengths), "base": args.checkpoint,
                      "label_review_complete": reviewed, "preparation_audit_ready": preparation is not None,
                      "ready_for_training": reviewed and preparation is not None,
                      "iterations": iterations, "gradient_accumulation": accumulation,
                      "requested_gradient_accumulation": args.gradient_accumulation,
                      "validation_positive_examples": sum(bool(row['target']['risks']) for row in valid)}))
    if args.preflight_only:
        return
    if args.output.exists():
        raise ValueError("Choose a new training output directory")
    args.output.mkdir(parents=True)
    data = args.output / "data"
    data.mkdir()
    for name, rows in [("train", train), ("valid", valid)]:
        (data / f"{name}.jsonl").write_text(''.join(json.dumps({"messages": row["messages"]}, ensure_ascii=False) + '\n' for row in rows))
    config = {"model": str(args.model_dir.resolve()), "data": str(data.resolve()), "train": True,
              "fine_tune_type": "lora", "batch_size": 1, "grad_accumulation_steps": accumulation,
              "iters": iterations, "learning_rate": args.learning_rate,
              "max_seq_length": args.max_seq_length, "mask_prompt": True, "grad_checkpoint": True,
              "num_layers": -1, "seed": 3407, "steps_per_report": 1, "steps_per_eval": 10,
              "val_batches": -1, "save_every": 10, "adapter_path": str((args.output / "adapters").resolve()),
              "lora_parameters": {"rank": 16, "scale": 2.0, "dropout": 0.0}}
    import yaml
    config_path = args.output / "training.yaml"
    config_path.write_text(yaml.safe_dump(config))
    record = {"status": "started", "experimental": args.allow_generated_labels,
              "label_review": "unreviewed_machine_labels" if args.allow_generated_labels else "human_reviewed", "base_checkpoint": args.checkpoint, "base_provenance": provenance,
              "trained_through": max(row["as_of"] for row in train + valid),
              "gradient_training_through": max(row["as_of"] for row in train),
              "training_data_sha256": hashlib.sha256((args.dataset / "train.jsonl").read_bytes()).hexdigest(),
              "risk_types": sorted({t for row in train for t in row["input"]["allowed_risk_types"]}),
              "packages": {name: importlib.metadata.version(name) for name in ("mlx", "mlx-lm", "transformers")}}
    record.update(preparation_manifest_sha256=hashlib.sha256(args.preparation_manifest.read_bytes()).hexdigest(),
                  dataset_version=preparation.get('dataset_version'),
                  requested_epochs=args.epochs, effective_sample_passes=config['iters']/len(train),
                  requested_gradient_accumulation=args.gradient_accumulation, actual_gradient_accumulation=accumulation,
                  validation_data_sha256=hashlib.sha256((args.dataset/'validation.jsonl').read_bytes()).hexdigest())
    record_path = args.output / "training-run.json"
    record_path.write_text(json.dumps(record, indent=2))
    try:
        subprocess.run([sys.executable, str(Path(__file__).with_name("mlx-slm-worker.py")), "--config", str(config_path)], check=True)
    except BaseException:
        record["status"] = "failed"
        record_path.write_text(json.dumps(record, indent=2))
        raise
    record["status"] = "experimental_adapter_trained" if args.allow_generated_labels else "adapter_trained"
    record_path.write_text(json.dumps(record, indent=2))
    print(f"Adapter trained in {args.output}. Export and held-out evaluation are still required; no production manifest was issued.")


if __name__ == "__main__":
    main()
