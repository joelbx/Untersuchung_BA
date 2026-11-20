Added a `metadata` config section with `check_for_updates`, defaulting to `true`. The loader now accepts the setting from YAML and JSON, and the config tests cover the default and explicit `false` values.

Verification: `go test ./config` and `git diff --check` pass.