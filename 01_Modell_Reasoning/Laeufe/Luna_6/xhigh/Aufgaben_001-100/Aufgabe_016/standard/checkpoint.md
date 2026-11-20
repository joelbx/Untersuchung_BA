# Host-scoped scheduling checkpoint

Implemented:
- Added `OlAsyncIOScheduler` with UTC configuration, monitoring job listeners, and function-name default job IDs.
- Made `limit_server` read `HOSTNAME`, support exact and trailing-prefix patterns, and match host short names against FQDNs. A disallowed job is removed or skipped at registration.
- Converted the monitoring entry point to an async scheduler service and registered an HAProxy collection job.
- Added `haproxy_monitor.py` with HAProxy CSV capture, Graphite event serialization, buffering, aggregation, dry-run output, and Graphite pickle transport.
- Added Docker container IP lookup with Compose service-name normalization.

Validation:
- `python -m pytest -q scripts/monitoring/tests`: 5 passed.
- `ruff check scripts/monitoring/utils.py scripts/monitoring/monitor.py scripts/monitoring/haproxy_monitor.py`: passed.
- `python -m py_compile ...` and `git diff --check`: passed.
