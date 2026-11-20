# Checkpoint

Task: register `flipt.is_auth_method` for Rego and bundle authorization engines.

Implemented enum-backed labels `token`, `oidc`, `kubernetes`, `k8s`, `github`, `jwt`, and `cloud`; added direct and engine tests, including a protobuf `Authentication` input.

Verification: `GOPROXY=off go test -count=1 ./internal/server/authz/engine/... ./internal/server/authz/middleware/grpc/... && git diff --check` exited 0. The authorization engine and middleware packages passed without cached test results.
