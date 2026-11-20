Implemented HA database fallback and listing deduplication.

- The proxy now shuffles all matching servers, retries tunnel connectivity failures, and returns a clear error if none are reachable. Tests can inject ordering, and the fake tunnel can simulate per-server outages.
- Added name deduplication for `tsh db ls`, stable name and host ID sorting, and host IDs in database server strings.
- Added tests for deduplication, fallback, and the all-candidates-offline error.

All relevant API, reverse tunnel, DB proxy, and `tsh` tests passed with sequential, process-capped runs. `git diff --check` passed.