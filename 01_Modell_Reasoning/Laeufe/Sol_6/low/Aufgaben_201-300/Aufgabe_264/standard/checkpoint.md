Task: Resolve Meraki API retry handling for HTTP 429/500/502, expose status, and report rate limit retries.
Completed: Added public HTTP exception classes, bounded retries with backoff, rate limit warning, and unit coverage for failure and recovery. Existing Meraki unit tests pass (9 passed).
