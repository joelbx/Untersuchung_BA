# Checkpoint

Implemented `-wp-ignore-inactive` and the `WpIgnoreInactive` global configuration setting. `FillWordPress` filters inactive packages before plugin/theme API requests, using either the CLI/global setting or the existing per-server `wordpress.ignoreInactive` setting. `removeInactives` returns `nil` when every package is inactive. The report-time filter also recognizes the global option.

Verification: `go test ./commands ./config ./models ./wordpress` passes. `git diff --check` passes. The first test invocation caught a pointer/slice compile mismatch in `FillWordPress`; that was corrected before the passing run.
