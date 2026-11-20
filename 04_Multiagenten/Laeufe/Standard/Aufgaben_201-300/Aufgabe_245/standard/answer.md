`detectScanDest` now returns a non-nil `map[string][]string` with ports grouped by IP, deduplicated, and sorted. Its scan consumer accepts the map and scans addresses in deterministic order. The existing tests were updated and expanded to cover overlapping wildcard addresses and duplicate ports.

Verification: `GOPROXY=off go test ./scan -count=1` passed.