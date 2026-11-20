# Checkpoint

Task: resolve host-scoped background job scheduling in `/app`.

Implemented:
- Added `OlAsyncIOScheduler` with UTC configuration, job listeners, and function-name default job IDs while retaining `OlBlockingScheduler` compatibility.
- Updated `limit_server` to read `HOSTNAME` via `os.environ.get`, match exact/prefix patterns against both full and short hostnames, and skip nonmatching registrations.
- Updated the monitoring entry point to use the asyncio scheduler and expose `monitor_haproxy` and async `main`.
- Added Docker service IP lookup and HAProxy CSV collection/Graphite event interfaces.

Verification: `python -m pytest scripts/monitoring/tests/test_utils_py.py -q` passed (2 tests); `python -m compileall -q scripts/monitoring` passed. No git history or index changes made.
