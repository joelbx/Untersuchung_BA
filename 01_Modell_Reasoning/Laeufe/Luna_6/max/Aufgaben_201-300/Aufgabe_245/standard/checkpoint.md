# Checkpoint

Task: Refactor `detectScanDest` to return an IP-to-ports map, deduplicate and deterministically order ports, return an empty map when no listeners exist, and update consumers.

Completed:
- `detectScanDest` now returns `map[string][]string`, expands wildcard addresses, merges duplicate ports, and sorts each IP's ports.
- `execPortsScan` now consumes the map and visits addresses in sorted order.
- Updated `Test_detectScanDest` expectations and added multi-port/deduplication coverage.

Verification: `GOPROXY=off go test ./scan` passed.
