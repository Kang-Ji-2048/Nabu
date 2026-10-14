#!/bin/bash
# Prepare/check only. Starting labelled-data training is a separate command.
set -euo pipefail
if [[ $# -gt 1 || ( $# -eq 1 && "$1" != --calibrate-gpu ) ]]; then
  echo 'Usage: bash scripts/prepare-epoch1.sh [--calibrate-gpu]' >&2
  exit 2
fi
nabu_root=$(cd "$(dirname "$0")/.." && pwd)
nabu_python="$nabu_root/.venv-slm/bin/python"
if [[ ! -x "$nabu_python" ]]; then
  nabu_bootstrap="${NABU_PYTHON:-python3.14}"
  if ! command -v "$nabu_bootstrap" >/dev/null 2>&1; then
    echo 'Install Python 3.14 first, or set NABU_PYTHON to its executable path.' >&2
    exit 2
  fi
  "$nabu_bootstrap" -m venv "$nabu_root/.venv-slm"
fi
"$nabu_python" - <<'PY'
import platform, sys
if sys.version_info[:2] != (3, 14) or platform.system() != 'Darwin' or platform.machine() != 'arm64':
    raise SystemExit('This pinned environment requires native Apple Silicon macOS and Python 3.14.')
PY
"$nabu_python" -m pip install -r "$nabu_root/requirements/slm-mac.lock.txt"
"$nabu_python" -m pip install --no-deps -e "$nabu_root"
"$nabu_python" -m pip check
nabu_report=$(mktemp -d "$nabu_root/data/training/local-preflight.XXXXXX")
"$nabu_python" "$nabu_root/scripts/check-reviewed-data.py" > "$nabu_report/data-check.json"
"$nabu_python" "$nabu_root/scripts/check-external-reference.py" > "$nabu_report/external-reference-check.json"
export HF_HOME="${HF_HOME:-$nabu_root/data/huggingface}"
nabu_model="$nabu_root/data/models/qwen3-8b-mlx-4bit"
if [[ ! -e "$nabu_model" ]]; then
  "$nabu_python" "$nabu_root/scripts/prepare-slm-model.py" --checkpoint Qwen/Qwen3-8B \
    --revision b968826d9c46dd6066d109eabc6255188de91218 --output "$nabu_model"
fi
nabu_dataset="$nabu_root/data/training/xd-assistant-reviewed-v3"
"$nabu_python" "$nabu_root/scripts/train-slm-mlx.py" --checkpoint Qwen/Qwen3-8B \
  --base-revision b968826d9c46dd6066d109eabc6255188de91218 \
  --dataset "$nabu_dataset" --model-dir "$nabu_model" \
  --preparation-manifest "$nabu_dataset/preparation-manifest.json" \
  --output "$nabu_report/unused-training-output" --preflight-only > "$nabu_report/training-preflight.json"
"$nabu_python" - <<'PY' > "$nabu_report/metal-check.json"
import json
import mlx.core as mx
if mx.default_device() != mx.gpu:
    raise SystemExit('Metal GPU is unavailable; run outside a filesystem sandbox or translated Intel shell.')
result = mx.sum(mx.arange(128))
mx.eval(result)
if result.item() != 8128:
    raise SystemExit('Metal computation check failed')
print(json.dumps({'device': str(mx.default_device()), 'metal_check': 'passed', 'training_started': False}))
PY
if [[ $# -eq 1 ]]; then
  "$nabu_python" "$nabu_root/scripts/check-slm-gpu.py" --model-dir "$nabu_model" \
    --sequence-length 8192 --output "$nabu_report/gpu-calibration.json"
fi
echo "Preparation passed. Reports: $nabu_report"
echo 'Labelled-data training has not started. When ready, run:'
echo 'bash scripts/start-epoch1.sh data/training/run-epoch1'
