Updated [scan/base.go](/app/scan/base.go:744) so `detectScanDest` returns an empty or populated `map[string][]string` with unique, sorted ports for each IP. Updated `execPortsScan` to consume the map, and expanded the [tests](/app/scan/base_test.go:280) for duplicates and wildcard addresses.

`go test ./scan -count=1` passed.