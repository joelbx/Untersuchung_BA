# Checkpoint

Task: add enabled audit sinks to anonymous telemetry and update schema version to 1.3.

Initial findings: telemetry lives in `internal/telemetry`; current version is 1.2. `rg` is unavailable, so repository searches use `grep` and `find`.

Status: complete. The `flipt` telemetry object now includes `audit: {"sinks": [...]}` only for enabled audit sinks. Schema version is 1.3. Tests cover log only, webhook only, both, and neither (including configured but disabled sinks).

Checks passed: `GONOSUMDB='*' GOPROXY=off go test ./internal/telemetry`; `GOPROXY=off go test ./internal/config ./internal/telemetry`; `git diff --check`.

The Go test command added checksum lines to `go.work.sum`; restored that unrelated working-tree change from HEAD.
