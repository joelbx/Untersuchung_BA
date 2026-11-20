`detectScanDest` now returns a `map[string][]string` with deduplicated, sorted ports for each IP. The port scanner consumes the new format, and the existing tests cover wildcard expansion and duplicate ports.

Verification passed: `go test ./scan -count=1` and `git diff --check`.