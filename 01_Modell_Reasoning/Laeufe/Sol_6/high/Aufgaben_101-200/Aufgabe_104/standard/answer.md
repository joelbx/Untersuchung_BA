Added `Config.Metadata.CheckForUpdates`, defaulting to `true`. The loader now accepts `metadata.check_for_updates` in YAML and JSON; the sample config and tests cover the setting.

Verified with `go test ./config ./cmd/flipt` and `git diff --check`.