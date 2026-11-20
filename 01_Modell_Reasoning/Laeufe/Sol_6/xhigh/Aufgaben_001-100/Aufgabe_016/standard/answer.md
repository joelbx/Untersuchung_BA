Implemented host-scoped monitoring in [utils.py](/app/scripts/monitoring/utils.py): `OlAsyncIOScheduler` now gives scheduled jobs function-name IDs, and `limit_server` checks `HOSTNAME` for exact names, trailing prefix wildcards, and short-name matches against FQDNs before registration.

The [monitoring entrypoint](/app/scripts/monitoring/monitor.py) now uses the asyncio scheduler and includes the scheduled [HAProxy collector](/app/scripts/monitoring/haproxy_monitor.py). The previous decorator order remains supported.

Verification: all 8 monitoring tests passed; Ruff, compilation, and `git diff --check` passed. Host-specific import checks registered the expected jobs. Live HAProxy and Graphite connections were not exercised.