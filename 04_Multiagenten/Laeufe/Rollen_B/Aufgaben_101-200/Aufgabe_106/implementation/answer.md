Updated the WordPress scan to read `IgnoreInactive` from the scan result’s server configuration. Cache lookups now use the map directly; a nil cache entry returns `""` with `ok == false`, while a cached empty string remains a valid hit. Added tests for those cache cases and for active and inactive themes and plugins.

`go test ./wordpress ./models ./report` and `git diff --check` passed.