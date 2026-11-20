#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
if (( $# < 2 )); then
    echo "Usage: bash run_skills_batch.sh {01|02|03} {controls|prepare|models|resume|check|stop|report} [options]" >&2
    exit 64
fi
block="$1"
phase="$2"
shift 2
case "$block" in
    01) tasks=1-100 ;;
    02) tasks=101-200 ;;
    03) tasks=201-300 ;;
    *) echo "Unknown block: $block" >&2; exit 64 ;;
esac
exec .venv/bin/python run_skills.py "$phase" --batch "batch-$block" --tasks "$tasks" "$@"
