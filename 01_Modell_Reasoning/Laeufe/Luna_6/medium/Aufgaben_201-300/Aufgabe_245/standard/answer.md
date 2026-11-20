Updated `detectScanDest` to return grouped `map[string][]string` results, with ports deduplicated and sorted per IP. Updated the scan consumer to accept the map and dial addresses in deterministic order.

Added coverage for empty results, duplicate ports, and sorted multi-port results. `go test ./scan` and `git diff --check` pass.