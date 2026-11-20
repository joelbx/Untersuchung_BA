Implemented anonymous telemetry with opt-out configuration, persistent UUID state, periodic `flipt.ping` reports, and the `internal/info.Flipt` HTTP handler. The advanced config example disables telemetry.

Verified with `go test ./config ./internal/info ./telemetry ./cmd/flipt`; all passed.