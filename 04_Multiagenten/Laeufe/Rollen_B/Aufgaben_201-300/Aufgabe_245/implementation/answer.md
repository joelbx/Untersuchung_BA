Refactored `detectScanDest` to return `map[string][]string`. It expands wildcard addresses, deduplicates and sorts each IP’s ports, and returns an empty map when there are no destinations. Updated `execPortsScan` to consume the map and extended the destination tests.

The focused scan tests passed offline, and `git diff --check` passed.