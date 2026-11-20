#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
if (( $# != 1 )); then
    echo "Usage: bash run_sol_ultra_201_300.sh {prepare|models|resume|stop|report|check}" >&2
    exit 64
fi
case "$1" in
    prepare|models|resume|stop|report|check)
        exec .venv/bin/python run_sol_ultra.py "$1" --tasks 201-300 --batch batch-03 --model-workers 5 ;;
    *) echo "Unknown phase: $1" >&2; exit 64 ;;
esac
