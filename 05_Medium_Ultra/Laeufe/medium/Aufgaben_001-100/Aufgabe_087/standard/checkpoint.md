# Checkpoint

Task complete: added opt-out anonymous telemetry, persisted UUID and timestamp, four-hour background reporting, and `internal/info.Flipt` HTTP handler. Wired reporter into server startup; telemetry errors are logged without stopping the server. Added config examples and tests.
Verification: `GOPROXY=off go test ./config ./telemetry ./internal/info ./cmd/flipt` passed; `git diff --check` passed.
