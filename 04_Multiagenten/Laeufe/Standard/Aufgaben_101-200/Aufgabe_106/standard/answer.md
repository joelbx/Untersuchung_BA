Updated the WordPress scan to pass the cache map directly and treat a present nil value as a cache miss. Package filtering now uses each package’s `Status` and the per-server `IgnoreInactive` setting, keeping active plugins and themes.

Added coverage for cache misses, nil values, and per-server filtering. `go test ./wordpress ./report ./models` passed with network access disabled.