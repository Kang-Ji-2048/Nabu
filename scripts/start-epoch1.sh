#!/bin/bash
set -euo pipefail
if [[ $# -ne 2 ]]; then
  echo 'Usage: scripts/start-epoch1.sh APPROVED_DATASET_DIRECTORY NEW_RUN_DIRECTORY' >&2
  exit 2
fi
nabu_root=$(cd "$(dirname "$0")/.." && pwd)
nabu_python="$nabu_root/.venv-slm/bin/python"
nabu_dataset="$1"
nabu_output="$2"
common=(--checkpoint Qwen/Qwen3-8B --dataset "$nabu_dataset" --model-dir "$nabu_root/data/models/qwen3-8b-mlx-4bit" --preparation-manifest "$nabu_dataset/preparation-manifest.json" --output "$nabu_output" --epochs 1 --max-seq-length 8192 --learning-rate 0.0001 --gradient-accumulation 8)
"$nabu_python" "$nabu_root/scripts/train-slm-mlx.py" "${common[@]}" --preflight-only
"$nabu_python" "$nabu_root/scripts/train-slm-mlx.py" "${common[@]}"
