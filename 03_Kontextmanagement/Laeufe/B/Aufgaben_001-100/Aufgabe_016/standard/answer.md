Implemented host-scoped job registration using the environment’s `HOSTNAME`, with exact, trailing-prefix wildcard, and short-name-to-FQDN matching. The monitoring service now uses `OlAsyncIOScheduler`, and the HAProxy metric interfaces are in place.

Validation passed: **5 monitoring tests**, lint checks, and local host-registration and CSV parsing checks.