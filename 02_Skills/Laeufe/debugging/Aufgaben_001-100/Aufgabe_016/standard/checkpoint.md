# Checkpoint

Task: implement host-scoped monitoring jobs in `/app`.

Status: investigating repository code and tests. `rg` is unavailable (`/bin/bash: rg: command not found`), so searches use `find`/`grep`.

Root cause: `monitor.py` uses `OlBlockingScheduler`, while `limit_server` is placed outside `scheduled_job` and removes a job only after registration. The host filter cannot prevent the original registration. The existing Python tests verify only final job presence and therefore miss that behavior. There is no HAProxy Python monitor yet. Existing HAProxy service is named `web_haproxy` in `compose.production.yaml`.

Pattern: the existing scheduler overrides `add_job` to use function names as IDs and attaches job listeners. Preserve those behaviors in an asyncio scheduler. Use decorator metadata with `limit_server` inside `scheduled_job` for conditional registration; retain outer-order compatibility for existing callers.

Hypothesis: moving host evaluation before `scheduled_job` calls `add_job` prevents registration on other hosts, while an asyncio scheduler permits the new coroutine job.

Implemented: `OlAsyncIOScheduler` shares UTC/job-listener/function-ID behavior with the legacy scheduler. `limit_server` records the environment-derived host match, and `scheduled_job` skips `add_job` for disallowed hosts when the limiter is the inner decorator. Existing outer-decorator callers still remove the already registered job for compatibility. Converted monitoring jobs to asyncio, added `monitor_haproxy`, `get_service_ip`, and the HAProxy CSV/Graphite collector.

Verification: The new host-scoping test failed before the scheduler change with `ImportError: cannot import name 'OlAsyncIOScheduler'`. The new HAProxy test failed before its module existed with `ModuleNotFoundError`. After implementation, `python -m pytest -q scripts/monitoring/tests` passed (10 tests); `python -m ruff check scripts/monitoring/utils.py scripts/monitoring/monitor.py scripts/monitoring/haproxy_monitor.py scripts/monitoring/tests/test_host_scoping.py scripts/monitoring/tests/test_haproxy_monitor.py` passed; `git diff --check` passed. Importing `scripts.monitoring.monitor` under `HOSTNAME=ol-www0.us.archive.org` yielded the three existing www jobs plus `monitor_haproxy`; under `HOSTNAME=ol-web0.us.archive.org` it yielded only `log_workers_cur_fn`.

Tooling: `rg` unavailable; used `find`/`grep`. `aiohttp` unavailable, so the collector uses existing `requests` in a thread and an asyncio Graphite socket. No check blocked.
