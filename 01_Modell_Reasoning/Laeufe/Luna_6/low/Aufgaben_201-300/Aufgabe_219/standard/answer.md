Implemented token audit event support. The checker recognizes `token:created` and `token:deleted`, and wildcard resource events include token. gRPC initialization checks whether `token:deleted` is enabled and passes that boolean to the authentication server, which gates deletion audit emission on it.

Verification passed: `go test ./internal/server/audit ./internal/server/auth ./internal/cmd`.