# Checkpoint

Task: implement host-scoped monitoring job registration and requested HAProxy monitoring interfaces in `/app`.
Status: implementation complete. `OlAsyncIOScheduler` uses UTC, listener messages, and function-name job IDs. `limit_server` checks `os.environ.get("HOSTNAME")` against exact names and trailing-prefix wildcards, including short host matches for FQDNs. The monitoring entrypoint uses the async scheduler and registers the HAProxy job on `ol-www0`. Added HAProxy CSV capture, Graphite event serialization, buffering and optional aggregation/sending, and Docker container IP lookup.

Checks run:
- `python -m pytest -q scripts/monitoring/tests`: 9 passed.
- `ruff check scripts/monitoring/utils.py scripts/monitoring/monitor.py scripts/monitoring/haproxy_monitor.py scripts/monitoring/tests/test_utils_py.py scripts/monitoring/tests/test_haproxy_monitor.py`: passed.
- `ruff format` applied to those files.
- `git diff --check`: passed.
- `HOSTNAME=ol-www0.us.archive.org python - <<'PY' ...`: confirmed `OlAsyncIOScheduler` and four expected registered jobs, including `monitor_haproxy`.

Tooling limits:
- `rg` command failed with `/bin/bash: line 1: rg: command not found`; used `find` and `grep` for local search.
- `black --check scripts/monitoring/utils.py scripts/monitoring/monitor.py scripts/monitoring/haproxy_monitor.py scripts/monitoring/tests/test_utils_py.py scripts/monitoring/tests/test_haproxy_monitor.py` failed with `/bin/bash: line 1: black: command not found`. Black formatting remains unverified; Ruff formatting and lint passed.
