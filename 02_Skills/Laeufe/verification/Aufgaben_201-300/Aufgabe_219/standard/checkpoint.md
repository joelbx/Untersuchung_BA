# Checkpoint

Task: Add audit support for token creation and deletion, including configuration mapping and gRPC wiring.

Changes:
- Added token to the audit event checker resource map and wildcard expansion.
- Added a token deletion event check during gRPC initialization and passed the resulting boolean to the authentication server.
- Made the authentication server use that boolean to gate deletion audit events.
- Added checker and authentication server tests, and documented the token resource.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./internal/server/audit ./internal/server/auth ./internal/cmd` passed (audit and cmd cached on final run; all three passed uncached in an earlier run after production edits).
- `git diff --check` passed.

Environment: `rg` unavailable; used `grep` and `find` for local searches. No offline tooling blocker remains.
