Refactored `detectScanDest` to return `map[string][]string` with deduplicated, sorted ports and an empty map when no ports are found. Updated `execPortsScan` to consume the map and expanded the existing tests to cover wildcard overlap.

`go test ./scan -count=1` passed.