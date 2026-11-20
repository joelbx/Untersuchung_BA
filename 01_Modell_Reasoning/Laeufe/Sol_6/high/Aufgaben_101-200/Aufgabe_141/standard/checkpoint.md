# Checkpoint

Task: add `-wp-ignore-inactive` and skip inactive WordPress plugin/theme vulnerability lookups.

Completed:
- Added `WpIgnoreInactive` to config, TOML loading, and the report command flag.
- Filtered inactive packages in `FillWordPress` before WPVulnDB requests; filtering returns nil when nothing remains.
- Added regression tests for request paths, result packages, nil filtering, and TOML loading.
- Passed offline tests: `go test ./wordpress ./config ./commands ./report ./models` with GOPROXY=off and GOSUMDB=off.
