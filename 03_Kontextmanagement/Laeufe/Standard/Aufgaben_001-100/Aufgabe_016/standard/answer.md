Implemented host-scoped monitoring jobs in `/app`. The limiter reads `HOSTNAME` from the environment, supports exact names, trailing `*` prefixes, and short names against fully qualified hostnames. Disallowed jobs are skipped before registration; existing decorator order remains supported.

Added `OlAsyncIOScheduler`, Docker service IP lookup, and the HAProxy collector with Graphite events. The async monitoring entrypoint schedules the HAProxy job on `ol-www0`.

Verification: all 9 monitoring tests pass; Ruff and `git diff --check` pass.