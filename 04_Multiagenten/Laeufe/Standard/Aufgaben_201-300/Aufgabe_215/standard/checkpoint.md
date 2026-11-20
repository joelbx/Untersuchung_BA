# Checkpoint

Task: add HTTPS configuration, validation, and serving support to Flipt.
Status: implementation complete; all Go tests pass.
Changes: path-based Viper configuration and validation; HTTP/HTTPS scheme and ports; TLS for REST/UI and gRPC; config documentation; focused config tests.
Verification: `go test ./cmd/flipt`, `go test ./...`, and `git diff --check` passed.
Constraints observed: local code and tests only; no history, index, or harness changes.
