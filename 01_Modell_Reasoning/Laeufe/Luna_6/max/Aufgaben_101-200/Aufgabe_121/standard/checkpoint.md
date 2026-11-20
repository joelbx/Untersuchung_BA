# Checkpoint

Task: add the `flipt.is_auth_method` Rego built-in for readable authentication method names.

Completed: registered the two-argument built-in in the local Rego engine. Supported labels map through generated protocol enum constants; `k8s` aliases `kubernetes`. The helper handles numeric and protobuf enum string inputs, returns false for mismatches, and returns the requested errors for missing authentication and unsupported labels.

Verification: `go test ./internal/server/authz/...` passed, including tests for each supported label, alias behavior, matching and mismatch results, protobuf enum strings, error messages, and engine integration.
