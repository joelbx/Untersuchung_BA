Updated the WordPress cache lookup to use the map directly and return `("", false)` for missing keys or nil values. The scan now reads `IgnoreInactive` from the server’s configuration, so inactive plugins and themes are excluded when that setting is enabled, while active packages remain included.

`go test ./wordpress ./models ./report` passed.