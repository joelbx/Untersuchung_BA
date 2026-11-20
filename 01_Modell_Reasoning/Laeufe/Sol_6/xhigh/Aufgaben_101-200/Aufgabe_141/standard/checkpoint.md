# Checkpoint

Task: add -wp-ignore-inactive configuration and filter inactive WordPress packages.
Status: inspecting repository.

Implementation in progress: added the setting to scan/report flags and TOML config; scan collection and report enrichment now filter inactive WordPress packages. Existing per-server ignoreInactive also uses early filtering. Next: focused tests and offline test run.

Completed: -wp-ignore-inactive is available for scan, report, and tui; wpIgnoreInactive loads from TOML with explicit CLI values taking precedence. Inactive plugins/themes are omitted from scan inventory and filtered before WPVulnDB requests during report enrichment. The helper returns nil for an empty result. Verified with GOPROXY=off GOSUMDB=off go test ./config ./wordpress ./models ./scan ./commands and go test ./report; all passed. git diff --check passed.
