# Checkpoint

Implemented host-scoped monitoring registration, an `OlAsyncIOScheduler`, Docker service IP lookup, and HAProxy CSV to Graphite collection. Added tests for hostname matching, scheduler job ids, monitoring host selection, HAProxy CSV parsing, and Docker container naming.

Inspection limitation: `rg` was attempted via `rg --files scripts/monitoring tests` and failed with `/bin/bash: line 1: rg: command not found`; local inspection continued with `find` and `grep`.

Verification (all executed after final code edits):
- `python -m pytest scripts/monitoring/tests -q` — exit 0, 9 passed.
- `python -m ruff check scripts/monitoring/utils.py scripts/monitoring/monitor.py scripts/monitoring/haproxy_monitor.py scripts/monitoring/tests/test_haproxy_monitor.py` — exit 0, all checks passed (existing pyproject deprecation warning).
- `python -m compileall -q scripts/monitoring/utils.py scripts/monitoring/monitor.py scripts/monitoring/haproxy_monitor.py` — exit 0.
- `git diff --check` — exit 0.

Live HAProxy and Graphite endpoints were not exercised; CSV parsing and job registration were checked locally.
