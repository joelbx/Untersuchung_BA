# Checkpoint

Task: Refactor `detectScanDest` to return IP-to-port maps, deduplicate ports with deterministic ordering, update consumers, and run relevant existing tests.

`detectScanDest` and its single consumer were found in `scan/base.go`. The function now builds a `map[string][]string`, deduplicates ports, sorts each port slice, and expands wildcard addresses. `execPortsScan` accepts the map and traverses IPs deterministically. Detection tests now assert the map result, including empty, multi-address, wildcard, and duplicate-port cases.

Validation: `gofmt` completed; `GOPROXY=off go test ./scan` passed. `git diff --check` passed. The test command emitted an existing SQLite C compiler warning, then reported `ok github.com/future-architect/vuls/scan`.
