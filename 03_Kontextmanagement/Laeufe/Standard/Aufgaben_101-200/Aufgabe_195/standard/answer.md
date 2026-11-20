Updated `Load` to return a `Result` with separate `Config` and `Warnings` fields. Deprecation warnings are now collected from keys explicitly present in the configuration file before defaults are applied, including `ui.enabled`. The CLI reads warnings from the result.

Verified with `go test ./internal/config ./cmd/flipt` and `git diff --check`.