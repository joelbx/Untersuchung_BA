Implemented the WordPress cache and filtering changes.

- [wordpress.go](/app/wordpress/wordpress.go) now looks up a direct cache map; missing keys and nil cached pointers return `("", false)`. Scanning uses the supplied per-server `WordPressConf` to filter packages by `Status`.
- [report.go](/app/report/report.go) passes each server’s WordPress configuration into the scan.
- [config.go](/app/config/config.go) now maps `ignoreInactive` from TOML.
- Updated cache tests to cover nil cached values.

`GOPROXY=off go test ./wordpress ./config ./report` passed. The report build emitted a SQLite C compiler warning, but its tests passed.