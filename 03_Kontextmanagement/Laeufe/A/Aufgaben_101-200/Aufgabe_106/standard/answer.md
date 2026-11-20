Updated the WordPress scan to look up cache entries directly, return `("", false)` for missing or nil entries, and filter inactive plugins and themes using the selected server’s configuration. The report CLI setting remains supported.

Added tests for nil cache entries and active/inactive packages. `go test ./wordpress ./report` passed with network access disabled.