Updated [scan/base.go](/app/scan/base.go) so `detectScanDest` returns `map[string][]string` with deduplicated, sorted ports and an empty map when no ports are found. The scan consumer now handles the map in deterministic IP order. Updated the existing tests in [scan/base_test.go](/app/scan/base_test.go).

Verification: `go test ./scan -count=1` passed with downloads disabled.