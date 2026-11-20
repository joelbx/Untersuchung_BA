`detectScanDest` now returns `map[string][]string`, deduplicates ports, and sorts each IP’s port slice. `execPortsScan` consumes the map and scans IPs in sorted order. Tests cover empty results, wildcard addresses, and multiple ports with duplicates.

Validation passed: `GOPROXY=off go test ./scan` and `git diff --check`.

Changed [scan/base.go](/app/scan/base.go:744) and [scan/base_test.go](/app/scan/base_test.go:280).