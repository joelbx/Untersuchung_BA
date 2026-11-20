Updated the WordPress cache lookup to use the map directly. It now returns `("", false)` for a missing key or a nil value, while a present empty string remains a cache hit. The scan now honors the server’s `WordPress.IgnoreInactive` setting and excludes inactive plugins and themes.

`GOPROXY=off GOSUMDB=off go test ./wordpress ./report` passed. No delegation was used.