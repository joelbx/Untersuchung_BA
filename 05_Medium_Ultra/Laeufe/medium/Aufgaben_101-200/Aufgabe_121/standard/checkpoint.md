# Checkpoint

Task: add `flipt.is_auth_method` Rego built-in with readable method names and coverage.

Status: implemented and verified. The new built-in maps all seven labels to generated protobuf enum constants, including the Kubernetes alias. Both local Rego and bundle engines load its registration. Direct tests cover every label, mismatches, and error messages; a local engine test evaluates the built-in in a policy.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/server/authz/engine/ext ./internal/server/authz/engine/rego ./internal/server/authz/engine/bundle` passed; `git diff --check` passed.
