`detectScanDest` now returns a map of IP addresses to deduplicated, sorted port slices, including an empty map when there are no destinations. The port scanner now consumes that map. I updated the [destination tests](/app/scan/base_test.go:280) to cover multiple ports and overlapping wildcard addresses.

Validation: `go test ./scan -count=1` and `git diff --check` passed.