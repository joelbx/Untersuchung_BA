# Checkpoint

Task: implement anonymous opt-out telemetry and Flipt HTTP handler.
Status: complete.
Changes: config telemetry fields and environment support; persisted UUID and timestamp; four-hour background ping; Flipt info handler; tests.
Verification: GOPROXY=off go test ./... passed; GOPROXY=off go test -race ./telemetry ./internal/info ./config passed; git diff --check passed.
