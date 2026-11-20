Implemented host-scoped monitoring jobs. `OlAsyncIOScheduler` now registers jobs only when `HOSTNAME` matches an allowed exact name or prefix wildcard, and registered jobs default to the function name as their ID. I also added the HAProxy metric collector and async monitoring entrypoint.

Verification: all 8 monitoring tests pass, Ruff passes, and `git diff --check` is clean.