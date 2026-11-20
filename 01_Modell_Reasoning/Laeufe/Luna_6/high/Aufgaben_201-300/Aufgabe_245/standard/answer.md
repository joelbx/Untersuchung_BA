`detectScanDest` now returns a map of IPs to deduplicated, sorted port slices. The scanner consumes that map and scans destinations in deterministic order. The existing tests cover empty results, grouping, sorting, and wildcard expansion.

Validation passed: `go test ./scan` and `git diff --check`.