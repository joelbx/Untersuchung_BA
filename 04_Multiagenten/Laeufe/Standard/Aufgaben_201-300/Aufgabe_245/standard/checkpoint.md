# Checkpoint

Task: Refactor detectScanDest to return deterministic, deduplicated ports grouped by IP and update consumers.
Status: Complete. detectScanDest returns a non-nil map, expands wildcard addresses, deduplicates and sorts port slices. execPortsScan accepts the map and scans addresses in sorted order. Existing scan tests updated and expanded.
Verification: GOPROXY=off go test ./scan -count=1 passed; git diff --check passed.
