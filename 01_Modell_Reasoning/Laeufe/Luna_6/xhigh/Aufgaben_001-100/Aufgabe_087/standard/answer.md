Implemented anonymous telemetry with default opt-in, environment overrides, persistent UUID state, four-hour reporting, and context-based shutdown. Added the `/meta/info` handler and disabled telemetry in the advanced config example.

`go test ./...` and `git diff --check` pass.

Key files: [telemetry.go](/app/telemetry/telemetry.go:75), [config.go](/app/config/config.go:118), [main.go](/app/cmd/flipt/main.go:225), [flipt.go](/app/internal/info/flipt.go:8).