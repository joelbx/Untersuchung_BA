#!/usr/bin/env bash
# Same standard-architecture settings as tasks 101–200; batch-03 adds 201–300.
# Default: controls only. Models must be started explicitly after validation.
set -euo pipefail

lab_directory="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$lab_directory"

phase="${1:-controls}"
# User-approved failed reference controls, identical for every configuration.
# Keep all 100 task identities; these five remain unscored, with no replacements.
excluded_controls="217,218,258,261,285"
if [[ $# -gt 1 || ( "$phase" != controls && "$phase" != models ) ]]; then
  echo "Usage: bash run_reasoning_201_300.sh [controls|models]" >&2
  exit 2
fi

for model in luna sol; do
  for effort in low medium high xhigh max; do
    echo "Reasoning batch-03: $model / $effort, tasks 201-300, phase $phase"
    if [[ "$phase" == controls ]]; then
      .venv/bin/python run_reasoning.py \
        --model "$model" --reasoning "$effort" \
        --batch batch-03 --tasks 201-300 \
        --exclude-invalid-controls "$excluded_controls" \
        --parallel-controls --control-workers 1
    else
      .venv/bin/python run_reasoning.py \
        --model "$model" --reasoning "$effort" \
        --batch batch-03 --tasks 201-300 \
        --exclude-invalid-controls "$excluded_controls" \
        --parallel --model-workers 5 --run
    fi
  done
done
