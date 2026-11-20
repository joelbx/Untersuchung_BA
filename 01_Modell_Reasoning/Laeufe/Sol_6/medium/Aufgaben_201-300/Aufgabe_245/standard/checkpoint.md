# Checkpoint

Task: Refactor scan destination detection to group deduplicated, ordered ports by IP and update consumers.
Status: Complete. `detectScanDest` now returns `map[string][]string`, expands wildcard listeners, deduplicates and sorts ports, and returns an empty map when no listeners exist. `execPortsScan` consumes the map in sorted IP order. Updated existing tests to cover the new shape, empty input with configured addresses, and wildcard overlap. `GOPROXY=off GOSUMDB=off go test ./scan -count=1` and `git diff --check` pass.
