Task: Add audit logging support for token creation/deletion events.
Status: Complete. Checker recognizes token and wildcard token pairs. gRPC setup derives token deletion audit flag from configured checker and passes it to authentication server. Added checker coverage for explicit and wildcard token events.
Verification: go test ./internal/server/audit ./internal/server/auth ./internal/cmd (passed); git diff --check (passed).
