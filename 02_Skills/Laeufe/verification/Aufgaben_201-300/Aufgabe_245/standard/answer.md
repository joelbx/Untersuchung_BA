Refactored `detectScanDest` to return IPs mapped to deduplicated, sorted port slices. It returns an empty map when there are no destinations, and `execPortsScan` now consumes the grouped map. Updated the existing tests and added coverage for wildcard overlap and the dial consumer.

Verification: `go test ./scan -count=1` passed offline, and `git diff --check` found no issues.