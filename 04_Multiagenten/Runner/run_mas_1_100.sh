#!/usr/bin/env bash
# Separate, explicit phases; never start models automatically after controls.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

if (( $# != 1 )); then
    echo "Usage: bash run_mas_1_100.sh {controls|models|resume|stop|report}" >&2
    exit 64
fi

experiment=experiment-mas-sol6-medium
batch=batch-01
runner=(.venv/bin/python run_mas.py --experiment "$experiment" --batch "$batch" --tasks 1-100)

case "$1" in
    controls) exec "${runner[@]}" ;;
    models) exec "${runner[@]}" --run ;;
    resume) exec "${runner[@]}" --resume-from "$batch" --run ;;
    stop) exec .venv/bin/python run_mas.py --experiment "$experiment" --batch "$batch" --stop ;;
    report) exec .venv/bin/python compare_mas.py --experiment "$experiment" --batch "$batch" ;;
    *) echo "Unknown phase: $1. Choose controls, models, resume, stop or report." >&2; exit 64 ;;
esac
