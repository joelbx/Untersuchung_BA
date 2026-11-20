# Checkpoint

Task: decouple startup release/update checks, classify rc builds as non-release, align status and telemetry behavior.
Status: implemented in `internal/release/check.go` and `cmd/flipt/main.go`; focused tests passed.
Verification: `GOPROXY=off go test ./internal/release ./cmd/flipt ./internal/info`; `git diff --check`.
