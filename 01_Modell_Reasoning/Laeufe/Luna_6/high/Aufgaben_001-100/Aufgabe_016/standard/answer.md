Implemented host-scoped scheduling and the monitoring updates in [utils.py](/app/scripts/monitoring/utils.py) and [monitor.py](/app/scripts/monitoring/monitor.py). `OlAsyncIOScheduler` inherits from `AsyncIOScheduler`, jobs default to the function name, and host matching uses `HOSTNAME` with exact names, trailing `*` patterns, and short/FQDN matching.

Added the HAProxy Graphite collector in [haproxy_monitor.py](/app/scripts/monitoring/haproxy_monitor.py). Updated the required [checkpoint](/app/.codex-role-output/checkpoint.md).

Verification: monitoring tests passed (5/5); syntax compilation and `git diff --check` passed.