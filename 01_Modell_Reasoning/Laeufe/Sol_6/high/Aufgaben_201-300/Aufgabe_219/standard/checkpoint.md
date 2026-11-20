Task: Add token audit event support and config-aware deletion logging.
Status: Complete.
Changes: Checker recognizes token and includes it in resource wildcard expansion. gRPC initialization builds and reuses the checker, then passes whether token:deleted is enabled to both authentication server setup paths. Added checker and auth server audit behavior tests.
Verification: GOTOOLCHAIN=local GOPROXY=off go test ./internal/cmd ./internal/server/audit ./internal/server/auth ./internal/server/middleware/grpc (passed); git diff --check (passed).
