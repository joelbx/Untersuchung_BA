# Checkpoint

Task: add `flipt.is_auth_method` Rego built-in with documented string-to-enum mappings and error behavior.
Status: implemented and verified.
Changes: new extension package registers two-argument built-in; enum-backed mappings cover token, oidc, kubernetes/k8s, github, jwt, cloud; Rego engine imports extension and propagates built-in errors; unit and engine integration tests added.
Tests: `go test ./internal/server/authz/engine/ext ./internal/server/authz/engine/rego ./internal/server/authz/middleware/grpc` passed.
Delegation: none.
