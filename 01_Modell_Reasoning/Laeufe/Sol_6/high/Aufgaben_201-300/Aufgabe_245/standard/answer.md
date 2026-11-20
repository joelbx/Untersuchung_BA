Refactored `detectScanDest` to return a map of IP addresses to deduplicated, sorted port slices. It returns an empty map when no destinations are found. Updated `execPortsScan` to consume the map and scan addresses in a stable order, and expanded the tests to cover multiple ports and wildcard overlap.

Verification passed: `go test -mod=readonly ./scan` and `git diff --check`.