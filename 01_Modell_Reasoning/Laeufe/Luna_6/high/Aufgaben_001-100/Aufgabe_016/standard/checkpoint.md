# Host-scoped scheduling checkpoint

Investigate the monitoring scheduler and existing tests, then implement environment-based hostname allowlisting with exact, prefix-wildcard, and short-name/FQDN matching. Ensure registered jobs default to the function name. Run relevant existing tests and record the outcome here.

Implemented `OlAsyncIOScheduler`, hostname matching through `os.environ.get("HOSTNAME")`, pending/active job removal for nonmatching hosts, function-name default job IDs, async monitoring startup, Docker service IP lookup, and the HAProxy Graphite collector interfaces.

Verification: `python -m pytest scripts/monitoring/tests -q` passed (5 tests); `python -m py_compile` passed for the modified monitoring modules; `git diff --check` passed.

A direct runtime check also confirmed `OlAsyncIOScheduler` inherits `AsyncIOScheduler` and `.scheduled_job(...)` registers a retrievable job using the function name.
