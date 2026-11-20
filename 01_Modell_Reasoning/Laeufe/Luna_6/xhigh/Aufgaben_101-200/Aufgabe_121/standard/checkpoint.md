Progress checkpoint

- Task: implement readable authentication method matching in the Rego authorization engine.
- Added globally registered `flipt.is_auth_method(input, method)` in `internal/server/authz/engine/ext/extentions.go`.
- Supported labels map to generated protobuf enum constants: token, oidc, kubernetes/k8s, github, jwt, and cloud.
- Missing authentication returns `no authentication found`; unsupported labels return `unsupported auth method` with the supplied value.
- Imported the extension into the local Rego engine and added tests for all mappings, false matches, errors, and Rego registration.
- Verification: `go test ./internal/server/authz/...` passed.
