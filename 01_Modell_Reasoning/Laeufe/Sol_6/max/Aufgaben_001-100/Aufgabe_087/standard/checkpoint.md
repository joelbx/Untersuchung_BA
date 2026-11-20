# Checkpoint

Task: add opt-out anonymous telemetry with persisted state and HTTP info handler.

Status: complete. Implemented opt-out config/environment loading, stateful anonymous reporter, four-hour scheduling, startup wiring, moved /meta/info handler to internal/info, and documented opt-out. Tests: `GOPROXY=off go test ./...` passed; `GOPROXY=off go test -race ./telemetry` passed; `git diff --check` passed. Telemetry delivery uses the default Flipt endpoint at https://telemetry.flipt.io/v1/track; live delivery was not tested because external research/network use is blocked.
