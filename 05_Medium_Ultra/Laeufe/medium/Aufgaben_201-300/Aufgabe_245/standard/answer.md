`detectScanDest` now returns a `map[string][]string`, grouping ports by IP with duplicate ports removed and each port slice sorted. An empty result is an empty map. The scan consumer now accepts the map and visits IPs in sorted order.

I updated the tests to cover multiple ports and overlapping wildcard addresses. The full `scan` package tests passed offline, and `git diff --check` passed.