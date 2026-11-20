Implemented `-wp-ignore-inactive` and the `WpIgnoreInactive` configuration setting. When enabled, inactive plugins and themes are filtered before vulnerability API requests; the existing per-server `wordpress.ignoreInactive` setting still works. `removeInactives` returns `nil` when no packages remain.

The report-time inactive filter also recognizes the global setting.

Verification passed: `go test ./commands ./config ./models ./wordpress` and `git diff --check`.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)