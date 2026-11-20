# Checkpoint

Implemented opt-out telemetry configuration and environment overrides, persistent private `telemetry.json` state with a stable UUID, a four-hour reporter, startup wiring, and the `internal/info.Flipt` HTTP handler. The advanced example disables telemetry. State and transport failures are logged in the background and do not stop the server.

Verification: `GOPROXY=off go test ./...` passed. `git diff --check` passed. `rg` was unavailable (`/bin/bash: rg: command not found`), so repository searches used `find` and `grep`.

Operational uncertainty: the repository provides no telemetry receiver address or contract. The reporter uses `https://telemetry.flipt.io/v1/track` with an anonymous JSON event; external delivery could not be verified under the no-external-research constraint. If that endpoint is not provisioned, sends will fail and be logged without affecting the server.
