# Checkpoint

Task: Add audit logging support for token creation and deletion events.
Completed: Added token to audit checker mapping and wildcard expansion. Derived token deletion enablement from the configured audit checker and passed it to authentication gRPC initialization. Added checker and authentication deletion audit tests.
Verification: GOPROXY=off go test ./internal/server/audit ./internal/server/auth ./internal/server/middleware/grpc ./internal/cmd (passed); git diff --check (passed).
