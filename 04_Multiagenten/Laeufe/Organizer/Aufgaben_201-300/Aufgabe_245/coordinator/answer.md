`detectScanDest` now returns `map[string][]string`, grouping ports by IP, removing duplicates, and sorting each port slice. `execPortsScan` consumes the map and sorts IP addresses before dialing. Tests cover empty results and overlapping wildcard addresses.

`go test ./scan -count=1` passed. No delegation was used.