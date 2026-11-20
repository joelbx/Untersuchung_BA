Added `Metadata.CheckForUpdates` to the configuration. It defaults to `true` and can be set with `metadata.check_for_updates` in YAML or JSON. Updated the default configuration example and added loading tests for both formats.

`go test ./config` and `go test ./cmd/flipt ./config` pass.