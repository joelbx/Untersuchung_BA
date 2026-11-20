# Checkpoint

Task: implement host-scoped scheduling for monitoring jobs in `/app`.

Completed: added `OlAsyncIOScheduler` with UTC job listeners and default function-name IDs. `limit_server` reads `HOSTNAME` through `os.environ.get`, supports exact names and trailing prefix wildcards, matches short names against FQDNs, and skips registration with the updated decorator order; the previous order remains supported. Converted the monitoring entrypoint to asyncio, added the scheduled HAProxy collector, Graphite event serialization and CSV parsing, and Docker service IP lookup.

Verified: `python -m pytest scripts/monitoring/tests -q` (8 passed), `ruff check` on changed Python files, `python -m compileall -q scripts/monitoring`, and `git diff --check`. Import checks show expected jobs on ol-www0 and ol-web0 and no jobs on an unrelated host. No external research or downloads were used.
