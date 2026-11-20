Implemented host-scoped job registration using `HOSTNAME`, with exact, prefix wildcard, and short-name matches. The monitoring service now uses `OlAsyncIOScheduler`, and registered jobs default to their function names as IDs. I also added the HAProxy collector and Graphite event output.

All 5 existing monitoring tests pass, and `git diff --check` is clean.