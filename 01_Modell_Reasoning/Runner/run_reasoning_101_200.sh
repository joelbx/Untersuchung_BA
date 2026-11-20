#!/usr/bin/env bash
# Start only when the repaired batch controls and study exclusions are finalized.
set -euo pipefail
lab_directory="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$lab_directory"
for model in luna sol; do
  for effort in low medium high xhigh max; do
    echo "Reasoning batch-02: $model / $effort, tasks 101-200"
    .venv/bin/python run_reasoning.py \
      --model "$model" --reasoning "$effort" \
      --batch batch-02 --tasks 101-200 \
      --parallel-controls --control-workers 1
    .venv/bin/python run_reasoning.py \
      --model "$model" --reasoning "$effort" \
      --batch batch-02 --tasks 101-200 \
      --parallel --model-workers 5 --run
  done
done
