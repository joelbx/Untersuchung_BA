Added `Metadata.CheckForUpdates` to [config.go](/app/config/config.go), defaulting to `true`. The loader now accepts `metadata.check_for_updates` from YAML and JSON; the default YAML documents the setting.

Verified with `go test ./config` and `git diff --check`.