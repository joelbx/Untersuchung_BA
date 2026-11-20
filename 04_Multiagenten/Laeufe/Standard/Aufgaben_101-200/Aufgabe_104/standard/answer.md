Added `Metadata.CheckForUpdates` to the [configuration](/app/config/config.go), with a default of `true`. YAML and JSON files can set `metadata.check_for_updates` to `false`; the default configuration now documents the setting.

Added loading coverage for both formats. `go test ./config ./cmd/flipt` and `git diff --check` passed.