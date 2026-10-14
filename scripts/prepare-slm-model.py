"""Pin and convert the exact Qwen instruction checkpoint to MLX 4-bit."""
import argparse
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nabu.slm import CHECKPOINT, SUPPORTED_CHECKPOINTS


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--checkpoint', choices=SUPPORTED_CHECKPOINTS, default=CHECKPOINT)
    parser.add_argument('--revision', help='Exact source commit; pass the recorded revision to reproduce a prepared base')
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Model output exists; choose a new directory')
    from huggingface_hub import HfApi, snapshot_download
    revision = HfApi().model_info(args.checkpoint, revision=args.revision).sha
    source = snapshot_download(args.checkpoint, revision=revision,
                               allow_patterns=['*.json', '*.safetensors', '*.jinja', '*.txt'])
    from mlx_lm.convert import convert
    args.output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.'+args.output.name+'-', dir=args.output.parent))
    try:
        converted = staging/'model'
        convert(hf_path=source, mlx_path=str(converted), quantize=True, q_bits=4)
        (converted/'nabu-base.json').write_text(json.dumps({'checkpoint': args.checkpoint, 'revision': revision, 'bits': 4}, indent=2)+'\n')
        if args.output.exists():
            raise ValueError('Output appeared concurrently')
        os.rename(converted, args.output)
    finally:
        shutil.rmtree(staging)


if __name__ == '__main__':
    main()
