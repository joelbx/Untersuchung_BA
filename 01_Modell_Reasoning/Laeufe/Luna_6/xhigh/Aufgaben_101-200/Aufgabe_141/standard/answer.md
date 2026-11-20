Implemented `-wp-ignore-inactive` for scan, report, and TUI commands. The new `WpIgnoreInactive` setting loads from TOML; `FillWordPress` filters inactive packages using the current config, saved scan config, or existing per-server setting.

`removeInactives` returns `nil` when filtering leaves no packages. `git diff --check` passed.

Tests passed: `GOPROXY=off go test ./config ./wordpress ./commands ./report ./models`. The WordPress and commands packages have no test files.