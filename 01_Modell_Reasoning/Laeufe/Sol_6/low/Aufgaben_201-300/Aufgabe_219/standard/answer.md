Added `token` to the audit checker, including wildcard expansion for `token:created` and `token:deleted`. gRPC initialization now checks whether `token:deleted` is enabled and passes that result to the authentication server to control deletion audit logging.

The relevant existing tests passed: `go test ./internal/server/audit ./internal/server/auth ./internal/cmd`.