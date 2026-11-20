Implemented database pool option loading and `meta.check_for_updates` handling in [config.go](/app/config/config.go). Missing update-check configuration now defaults to `false`; other omitted fields continue to come from `Default()`.

Updated the advanced fixture and `TestLoad` expectations. The default and deprecated fixture tests still verify equality with `Default()`.

Verified with `go test ./config` and `git diff --check`; both passed.