Updated the WordPress scan to look up cache entries directly, treat a present nil entry as a miss, and read `IgnoreInactive` from the scanned server’s configuration. Package filtering now excludes entries with `Status="inactive"` while retaining active entries.

Added coverage for cache misses and per-server filtering. `go test ./wordpress ./report ./models` and `git diff --check` pass.