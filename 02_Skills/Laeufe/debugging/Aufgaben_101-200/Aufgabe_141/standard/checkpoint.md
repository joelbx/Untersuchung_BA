# Checkpoint

Task: Add `-wp-ignore-inactive` configuration and filter inactive WordPress plugins/themes from scan results.

Status: Investigating existing flag, config, and WordPress data flow before edits.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local alternatives.

Investigation:
- WordPress packages are collected by `scan/base.go` with WP-CLI status values.
- `wordpress.FillWordPress` loops over all themes/plugins and requests WPVulnDB for each; its TODO names this flag.
- Existing per-server `WordPress.IgnoreInactive` filters CVEs later in `models.FilterInactiveWordPressLibs`, after API requests, so it does not save calls.
- `ReportCmd.SetFlags` registers report flags; `config.TOMLLoader.Load` selectively copies decoded settings into `Conf`.
- Root cause: no global `WpIgnoreInactive` flag/config field, and no filtering before the API loops.
- Hypothesis: filtering the package list at the start of `FillWordPress` before iteration will prevent inactive package API calls and remove them from the resulting package list, while preserving the default behavior.

Implementation and verification:
- Added `WpIgnoreInactive` to global config, report `SetFlags`, usage, and TOML loader. The loader keeps a true CLI value when the TOML field is absent.
- Added `removeInactives`, returning nil when every package has inactive status.
- `FillWordPress` filters `WordPressPackages` before any WPVulnDB requests when the option is enabled.
- Regression test initially failed with requests to inactive theme/plugin endpoints and inactive entries still in results. After patch it passed.
- `GOPROXY=off GOSUMDB=off go test ./wordpress ./config ./commands ./report ./models -count=1` passed; sqlite3 C dependency emitted a compiler warning but tests exited 0.
- Final rerun of `GOPROXY=off GOSUMDB=off go test ./wordpress ./config ./commands ./report ./models -count=1` exited 0 across all five packages.
