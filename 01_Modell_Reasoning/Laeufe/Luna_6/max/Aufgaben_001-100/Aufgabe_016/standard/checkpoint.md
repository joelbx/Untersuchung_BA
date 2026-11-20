# Host-scoped scheduling checkpoint

- Objective: implement host-based scheduled job registration and the monitoring scheduler/HAProxy interfaces described in the issue.
- Repository was clean at the start; no `AGENTS.md` files were found under the workspace parent.
- Initial inspection: `rg` is unavailable, so file discovery uses `find` and standard shell tools.
- Implemented host allowlist matching in `scripts/monitoring/utils.py`, including exact names, trailing `*` prefixes, short names for FQDNs, safe skipping when `HOSTNAME` is unset, asyncio scheduler support, default function-name job IDs, and Docker service IP lookup.
- Added `scripts/monitoring/haproxy_monitor.py` with CSV parsing, capture filters, Graphite event serialization, buffering/aggregation, dry-run output, and Graphite pickle transport.
- Reworked `scripts/monitoring/monitor.py` to register host-scoped jobs on `OlAsyncIOScheduler` and start through an async entry point.
- Validation: `PYTHONPATH=. pytest -q scripts/monitoring/tests` passed (5 tests); Ruff passed on changed Python files; `python -m compileall -q scripts/monitoring` and `git diff --check` passed.
