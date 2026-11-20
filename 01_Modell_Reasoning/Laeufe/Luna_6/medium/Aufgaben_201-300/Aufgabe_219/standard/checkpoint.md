# Checkpoint

Implemented token audit support:
- `token` is a recognized audit resource and expands under `*` for all verbs.
- gRPC startup checks configured events for `token:deleted` and passes that boolean to the authentication service.
- Authentication deletion audit emission uses the token-specific enabled flag.
- Checker tests cover wildcard expansion and explicit token deletion selection.

Verification: `go test ./internal/server/audit ./internal/server/auth ./internal/cmd` passed; `git diff --check` passed.
