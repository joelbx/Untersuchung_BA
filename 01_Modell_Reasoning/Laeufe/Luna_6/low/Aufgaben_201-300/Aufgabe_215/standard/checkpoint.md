# Checkpoint

Task: add configurable HTTP/HTTPS serving and configuration validation for Flipt.

Implemented configurable `http`/`https`, TLS file checks, HTTP/HTTPS port defaults, path-based YAML loading with `FLIPT_*` environment overrides, and one-value/list CORS origin handling. Updated startup to select the configured port and TLS listener.

Verification: `go test ./cmd/flipt` and `go test ./server ./storage/...` pass. The C SQLite dependency emits its existing compiler warning. `git diff --check` passes.
