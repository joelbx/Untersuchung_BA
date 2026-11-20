`detectScanDest` now returns a `map[string][]string` with deduplicated, sorted ports for each IP. It returns an empty map when no ports are found. The port scan consumer now accepts the map, and the tests cover overlapping wildcard and specific addresses.

`go test ./scan -count=1` passed.