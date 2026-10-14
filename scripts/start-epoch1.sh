#!/bin/bash
set -euo pipefail
if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo 'Usage: scripts/start-epoch1.sh [REVIEWED_DATASET_DIRECTORY] NEW_RUN_DIRECTORY' >&2
  exit 2
fi
nabu_root=$(cd "$(dirname "$0")/.." && pwd)
nabu_python="$nabu_root/.venv-slm/bin/python"
if [[ $# -eq 1 ]]; then
  nabu_dataset="$nabu_root/data/training/xd-assistant-reviewed-v3"
  nabu_output="$1"
else
  nabu_dataset="$1"
  nabu_output="$2"
fi
[[ "$nabu_dataset" = /* ]] || nabu_dataset="$nabu_root/$nabu_dataset"
[[ "$nabu_output" = /* ]] || nabu_output="$nabu_root/$nabu_output"
if [[ ! -x "$nabu_python" ]]; then
  echo 'Run bash scripts/prepare-epoch1.sh first.' >&2
  exit 2
fi
"$nabu_python" "$nabu_root/scripts/check-reviewed-data.py" --dataset "$nabu_dataset"
common=(--checkpoint Qwen/Qwen3-8B --base-revision b968826d9c46dd6066d109eabc6255188de91218 --dataset "$nabu_dataset" --model-dir "$nabu_root/data/models/qwen3-8b-mlx-4bit" --preparation-manifest "$nabu_dataset/preparation-manifest.json" --output "$nabu_output" --epochs 1 --max-seq-length 8192 --learning-rate 0.0001 --gradient-accumulation 8)
"$nabu_python" "$nabu_root/scripts/train-slm-mlx.py" "${common[@]}" --preflight-only
"$nabu_python" "$nabu_root/scripts/train-slm-mlx.py" "${common[@]}"
