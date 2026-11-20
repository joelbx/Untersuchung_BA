# Checkpoint

Task completed: token is recognized by the audit event checker, including wildcard resource expansion. gRPC initialization checks the configured event list for `token:deleted` when audit sinks are enabled and passes the resulting boolean into authentication gRPC setup. The auth server uses that boolean for token deletion audit emission.

Added checker coverage for explicit token pairs, token-only and resource/action wildcards, plus an auth server test verifying token deletion emits an audit span event only when enabled.

Checks: `go test ./internal/server/audit ./internal/server/auth ./internal/server/middleware/grpc ./internal/cmd` passed. `git diff --check` passed.

Tooling: `rg` was unavailable (`/bin/bash: rg: command not found`), so local `find` and `grep` were used. An initial broad `go test` overlapped with an edit to `server_test.go` and failed to import newly added packages during that overlap; the final rerun of the same packages passed after edits were complete.
