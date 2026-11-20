#!/usr/bin/env bash
# Same MAS v1 protocol; separate immutable 300-task pool, batch-03.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
if (( $# != 1 )); then
    echo "Usage: bash run_mas_201_300.sh {controls|repair-controls|models|resume|stop|report}" >&2
    exit 64
fi
experiment=experiment-mas-sol6-medium-300
batch=batch-03
runner=(.venv/bin/python run_mas.py --experiment "$experiment" --batch "$batch" --pool 300 --tasks 201-300)
case "$1" in
    controls) exec "${runner[@]}" --parallel-controls --control-workers 5 ;;
    repair-controls) exec "${runner[@]}" --repair-controls --parallel-controls --control-workers 5 ;;
    models) exec "${runner[@]}" --parallel --model-workers 5 --run ;;
    resume) exec "${runner[@]}" --resume-from "$batch" --parallel --model-workers 5 --run ;;
    stop) exec "${runner[@]}" --stop ;;
    report) exec .venv/bin/python compare_mas.py --experiment "$experiment" --batch "$batch" ;;
    *) echo "Unknown phase: $1" >&2; exit 64 ;;
esac
