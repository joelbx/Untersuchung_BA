# Checkpoint

Task: Add Rego flipt.is_auth_method builtin with documented auth method strings and tests.
Status: Complete. Builtin registered for local and bundle authorization engines; all seven labels map to auth.proto enum constants; local engine propagates builtin errors.
Verification: go test ./internal/server/authz/engine/... ./internal/server/authz/middleware/grpc (passed); git diff --check (passed).
