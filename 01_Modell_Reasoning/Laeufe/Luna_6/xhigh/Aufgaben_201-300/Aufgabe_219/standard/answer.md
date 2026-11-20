Implemented token audit event support.

- Added `token` and wildcard expansion to the audit checker, enabling `token:created`, `token:deleted`, and `*:*`.
- Passed the checker’s `token:deleted` result into the authentication server so deletion events follow the configured audit events.
- Updated the audit documentation and checker coverage.

Validation passed: `go test ./internal/server/audit ./internal/server/auth ./internal/cmd`, `go test ./internal/server/middleware/grpc`, and `git diff --check`.