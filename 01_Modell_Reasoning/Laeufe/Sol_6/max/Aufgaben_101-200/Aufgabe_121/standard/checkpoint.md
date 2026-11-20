# Auth method policy builtin

Task: add and verify `flipt.is_auth_method` for readable authentication method names.

Initial state: clean working tree. Located the auth proto and Rego engine; inspecting registration and existing tests next.

Findings: auth.Method enum has TOKEN=1, OIDC=2, KUBERNETES=3, GITHUB=4, JWT=5, CLOUD=6. Both direct Rego and SDK bundle engines need the global registration. OPA suppresses built-in errors by default, so both evaluation paths need strict built-in errors for the requested error behavior.

Implemented: global `flipt.is_auth_method` registration in `internal/server/authz/engine/ext/extentions.go`; imports and strict error handling in both engines; tests for all labels, mismatches, aliases, argument shape, errors, bundle evaluation, and role scoping; example documentation.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/server/authz/...` passed. `git diff --check` passed. Working tree has only the intended authorization engine changes and new example files.
