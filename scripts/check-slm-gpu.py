"""Disposable synthetic GPU calibration; no ticket labels or trained artifact."""
import argparse
import json
from pathlib import Path
import tempfile
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--sequence-length', type=int, default=6667)
    args = parser.parse_args()
    if args.output.exists() or args.sequence_length < 65:
        raise ValueError('Choose a new report file and a sequence length >=65')
    import mlx.core as mx
    import mlx.nn as nn
    import mlx.optimizers as optim
    from mlx.utils import tree_flatten
    from mlx_lm import load
    from mlx_lm.tuner.trainer import default_loss, grad_checkpoint
    from mlx_lm.tuner.utils import linear_to_lora_layers
    from mlx_lm.utils import maybe_set_recommended_wired_limit
    _ = maybe_set_recommended_wired_limit()
    mx.random.seed(3407)
    model, _ = load(str(args.model_dir))
    model.freeze()
    linear_to_lora_layers(model, -1, {'rank': 16, 'scale': 2.0, 'dropout': 0.0})
    keys = [key for key, _ in tree_flatten(model.trainable_parameters())]
    if not keys or any(not key.endswith(('lora_a', 'lora_b')) for key in keys):
        raise ValueError('Unexpected trainable base weights')
    grad_checkpoint(model.layers[0])
    model.train()
    optimizer = optim.Adam(learning_rate=1e-4)
    value_and_grad = nn.value_and_grad(model, default_loss)
    records = []
    for length in (512, args.sequence_length):
        print(json.dumps({'status': 'synthetic_calibration', 'sequence_length': length}), flush=True)
        batch = mx.random.randint(100, 20000, (1, length))
        lengths = mx.array([[length-64, length]])
        started = time.perf_counter()
        (loss, target_tokens), gradients = value_and_grad(model, batch, lengths)
        optimizer.update(model, gradients)
        mx.eval(model.trainable_parameters(), optimizer.state, loss, target_tokens)
        elapsed = time.perf_counter()-started
        if not bool(mx.isfinite(loss).item()):
            raise ValueError('Nonfinite synthetic loss')
        record = {'sequence_length': length, 'elapsed_seconds': round(elapsed, 3), 'synthetic_loss': float(loss.item()),
                  'assistant_like_target_tokens': int(target_tokens.item()), 'peak_memory_gb': round(mx.get_peak_memory()/1e9, 3)}
        records.append(record)
        print(json.dumps(record), flush=True)
        mx.clear_cache()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.synthetic-adapter-', dir=args.output.parent) as directory:
        checkpoint = Path(directory)/'adapters.safetensors'
        weights = dict(tree_flatten(model.trainable_parameters()))
        mx.save_safetensors(str(checkpoint), weights)
        restored = mx.load(str(checkpoint))
        if set(restored) != set(weights) or not all(bool(mx.array_equal(weights[key], restored[key]).item()) for key in weights):
            raise ValueError('Adapter checkpoint roundtrip mismatch')
    report = {'status': 'synthetic_calibration_passed', 'device': str(mx.default_device()),
              'model_provenance': json.loads((args.model_dir/'nabu-base.json').read_text()),
              'ticket_labels_used': False, 'trained_artifact_persisted': False, 'synthetic_adapter_discarded': True,
              'adapter_checkpoint_roundtrip': 'passed', 'trainable_adapter_tensors': len(keys),
              'settings': {'rank':16,'batch_size':1,'gradient_checkpointing':True,'learning_rate':1e-4},
              'steps': records,
              'limitations': ['Synthetic calibration checks computation/memory and serialization, not risk-model quality.', 'Full-epoch timing depends on approved examples and validation overhead.']}
    args.output.write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
