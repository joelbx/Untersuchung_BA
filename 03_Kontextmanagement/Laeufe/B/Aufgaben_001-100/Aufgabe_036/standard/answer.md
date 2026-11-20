Resolved the config loader issue. `Load` now reads the three DB pool options and `meta.check_for_updates`; an absent update-check key defaults to `false`. The default fixtures still load field-for-field equal to `Default()`.

Verified with `go test ./config` and `git diff --check`.