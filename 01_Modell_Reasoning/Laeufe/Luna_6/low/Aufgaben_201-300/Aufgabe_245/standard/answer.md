Refactored `detectScanDest` to return `map[string][]string`, deduplicating and sorting each IP’s ports. Updated `execPortsScan` to consume the map and dial destinations in deterministic order.

Updated the existing `detectScanDest` test expectations. `git diff --check` passed. The `go test ./scan` and focused test commands did not finish during this run, so test results are unavailable.