Added `Metadata.CheckForUpdates` to the config, defaulting to `true`. The loader accepts `metadata.check_for_updates` and `metadata.checkForUpdates`; the config example and YAML/JSON tests cover the setting.

Verification: `go test ./config` passed.