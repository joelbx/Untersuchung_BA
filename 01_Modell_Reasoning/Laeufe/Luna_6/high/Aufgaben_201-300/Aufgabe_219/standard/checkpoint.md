# Checkpoint

Implemented token audit event support:
- `audit.Checker` accepts `token`, includes it in `*`, and has coverage for explicit token events, deletion wildcards, and `*:*`.
- Authentication gRPC setup computes `tokenDeletedEnabled` with `Checker.Check("token:deleted")` and passes the boolean to the authentication server in both registration paths.
- The authentication server emits token deletion audit events only when that boolean is true.
- Audit filter documentation lists `token` as a supported resource.

Verification: `go test ./internal/server/audit ./internal/server/auth ./internal/cmd` passed, and `git diff --check` passed.
