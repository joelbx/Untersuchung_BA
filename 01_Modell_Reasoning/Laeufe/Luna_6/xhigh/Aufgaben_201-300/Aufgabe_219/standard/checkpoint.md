# Checkpoint

Task: Add audit logging support for token creation and deletion events.

Completed:
- Added `token` to recognized audit resources and wildcard expansion, covering `token:created`, `token:deleted`, and all-event configurations.
- Reused the configured audit checker during gRPC setup and passed its `token:deleted` result into the authentication server; deletion events are emitted only when enabled.
- Documented token as an audit resource and extended checker tests for explicit and wildcard token events.

Validation passed:
- `go test ./internal/server/audit ./internal/server/auth ./internal/cmd`
- `go test ./internal/server/middleware/grpc`
- `git diff --check`
