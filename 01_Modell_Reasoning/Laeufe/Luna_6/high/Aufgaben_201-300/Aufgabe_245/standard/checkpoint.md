# Checkpoint

## Objective
Refactor `detectScanDest` to return deduplicated, deterministically ordered port slices grouped by IP, and update all consumers.

## Progress
- `detectScanDest` now returns `map[string][]string`, deduplicates ports per address, expands wildcard listeners to configured IPv4 addresses, and sorts each port slice.
- `execPortsScan` now accepts the grouped map and scans IPs and ports in sorted order.
- Updated existing detection tests for empty output, grouping, sorting, and wildcard deduplication.

## Validation
- `go test ./scan` passed.
- `git diff --check` passed.
