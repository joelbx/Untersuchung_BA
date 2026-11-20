# Checkpoint

Task: Add `-wp-ignore-inactive` configuration and filter inactive WordPress plugins/themes.

Implemented:
- Added `Config.WpIgnoreInactive`, TOML loading, and a generated config template example.
- Registered `-wp-ignore-inactive` for report and TUI, where WordPress vulnerability lookups run.
- `FillWordPress` filters inactive packages when the global option or existing per-server `wordpress.ignoreInactive` option is enabled. This skips inactive plugin/theme API calls and removes them from the result package list.
- Added `removeInactives`, which returns nil when all packages are inactive.

Verification: `go test ./config ./commands ./wordpress` passed; `git diff --check` passed. The Go build emitted a warning from the existing `go-sqlite3` C source.
