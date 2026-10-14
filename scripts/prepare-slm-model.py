"""Pin and convert the exact Qwen instruction checkpoint to MLX 4-bit."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.slm import CHECKPOINT, SUPPORTED_CHECKPOINTS


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--checkpoint', choices=SUPPORTED_CHECKPOINTS, default=CHECKPOINT)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Model output exists; choose a new directory')
    from huggingface_hub import HfApi, snapshot_download
    revision = HfApi().model_info(args.checkpoint).sha
    source = snapshot_download(args.checkpoint, revision=revision,
                               allow_patterns=['*.json', '*.safetensors', '*.jinja', '*.txt'])
    from mlx_lm.convert import convert
    convert(hf_path=source, mlx_path=str(args.output), quantize=True, q_bits=4)
    (args.output / 'nabu-base.json').write_text(json.dumps({'checkpoint': args.checkpoint, 'revision': revision, 'bits': 4}, indent=2) + '\n')


if __name__ == '__main__':
    main()
