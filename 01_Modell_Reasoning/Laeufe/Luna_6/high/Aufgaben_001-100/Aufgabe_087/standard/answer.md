Implemented anonymous telemetry with default-on opt-out configuration, stable UUID state in `telemetry.json`, and a background `flipt.ping` reporter. Added the `internal/info.Flipt` HTTP handler and wired telemetry into startup as a best-effort service. The advanced config explicitly disables telemetry.

Verification passed: `go test ./config ./telemetry ./internal/info ./cmd/flipt` and `git diff --check`. The telemetry and info packages have no existing dedicated tests.

One limitation: the reporting endpoint is set to `https://telemetry.flipt.io/v1/track`; the repository contains no endpoint configuration.