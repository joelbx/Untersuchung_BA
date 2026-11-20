Implemented host scoped scheduling and the requested monitoring interfaces.

- `limit_server` reads `HOSTNAME` from the environment and matches exact names, trailing `*` patterns, and short names against FQDNs.
- Added `OlAsyncIOScheduler` with job listeners and function name job IDs; updated the monitoring entry point to use it.
- Added the HAProxy collection and Graphite event interfaces, plus Docker service IP lookup.

Verification: the existing monitoring tests passed (2 tests), and `scripts/monitoring` compiled successfully.