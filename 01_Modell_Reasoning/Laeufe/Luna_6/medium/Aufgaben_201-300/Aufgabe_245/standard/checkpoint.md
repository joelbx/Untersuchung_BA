# Checkpoint

Implemented the scan destination refactor:
- `detectScanDest` returns `map[string][]string` and returns a non-nil empty map when no ports are found.
- Wildcard listeners expand across IPv4 addresses; ports are deduplicated and sorted per IP.
- `execPortsScan` consumes the grouped map, traverses IPs deterministically, and joins host and port safely.
- Updated and expanded `detectScanDest` tests for grouped results, duplicate removal, empty output, and ordering.

Verification: `go test ./scan` passes. `git diff --check` passes.
