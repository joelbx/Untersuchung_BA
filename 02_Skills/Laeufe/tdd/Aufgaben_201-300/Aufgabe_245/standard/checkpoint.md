# Checkpoint

Task completed: `detectScanDest` returns a non-nil `map[string][]string`, expands wildcard addresses, deduplicates ports per IP, and sorts ports numerically with a string fallback. `execPortsScan` consumes the grouped map and scans IPs in sorted order.

TDD red: `GOPROXY=off GOSUMDB=off go test ./scan -run '^Test_detectScanDest$' -count=1` failed as expected because the old result was a flat slice. `GOPROXY=off GOSUMDB=off go test ./scan -run '^Test_execPortsScanAcceptsGroupedDestinations$' -count=1` failed to compile as expected because the old consumer accepted a slice.

TDD green: `GOPROXY=off GOSUMDB=off go test ./scan -run '^(Test_detectScanDest|Test_execPortsScanAcceptsGroupedDestinations)$' -count=1` passed. `GOPROXY=off GOSUMDB=off go test ./...` passed. `git diff --check` passed.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used grep/find. Test runs emit a pre-existing compiler warning from bundled `github.com/mattn/go-sqlite3` C source (`sqlite3-binding.c:128049`, `-Wreturn-local-addr`); tests still passed.
