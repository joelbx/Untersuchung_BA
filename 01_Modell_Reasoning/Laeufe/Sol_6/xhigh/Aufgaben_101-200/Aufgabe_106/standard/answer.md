Resolved the WordPress scan issues. Cache lookup now uses the map directly and returns `("", false)` for a missing key or nil value. Plugin and theme filtering now uses the per-server `IgnoreInactive` setting and excludes packages whose `Status` is `"inactive"`.

Added tests for cache states and active/inactive package scanning. `GOPROXY=off go test ./wordpress ./report ./models` passed.