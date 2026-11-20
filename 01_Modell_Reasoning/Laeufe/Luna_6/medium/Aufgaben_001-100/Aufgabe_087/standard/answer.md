Implemented anonymous telemetry with a persistent per host UUID, four hour reporting, config and environment opt out, and startup integration. Added the `internal/info.Flipt` HTTP handler and explicitly disabled telemetry in the advanced config example.

Verification passed: `go test ./config ./telemetry ./internal/info`, `go test ./cmd/flipt`, and `git diff --check`.