# Auth method Rego builtin checkpoint

- Goal achieved: `flipt.is_auth_method(input, method)` is registered for Rego policies with seven allowed labels mapped to generated auth protobuf enum constants. `k8s` and `kubernetes` share the Kubernetes enum value.
- The builtin returns booleans for matches and mismatches. Missing authentication returns `no authentication found`; unsupported labels return `unsupported auth method: <value>`. These errors halt policy evaluation so callers receive them.
- Added direct builtin tests and an engine policy test using a protobuf authentication object and role metadata.
- Validation passed: `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/server/authz/...`; `git diff --check` passed.
