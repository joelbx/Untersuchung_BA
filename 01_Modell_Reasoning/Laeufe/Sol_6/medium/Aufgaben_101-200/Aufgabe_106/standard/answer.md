Updated the WordPress cache lookup to use a map directly and return `("", false)` for missing or nil entries. The scan now reads `IgnoreInactive` from its server configuration and excludes plugins and themes whose `Status` is `"inactive"` while retaining active packages.

Added tests for cache entries and both server settings. `go test ./wordpress ./report ./models` and `git diff --check` passed.