Task: add audit logging support for token creation and deletion events.
Status: complete. Added token and wildcard checker mappings, passed checker decision for token:deleted into the authentication gRPC server, documented token resource, and added checker cases for explicit and wildcard token events.
Verification: go test ./internal/server/audit ./internal/server/auth ./internal/cmd ./internal/server/middleware/grpc passed; git diff --check passed.
Constraints: local code/tests only; git history, index baseline, and harness configuration untouched.
