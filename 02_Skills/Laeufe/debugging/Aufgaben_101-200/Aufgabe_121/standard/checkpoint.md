# Checkpoint

Task: add Rego built-in `flipt.is_auth_method` for readable authentication methods.

Status: investigating root cause and local policy engine patterns. `rg` is unavailable; using local `find`/`grep`.

Root cause: neither authorization engine imports or registers a custom OPA built-in. A local regression test (`GOPROXY=off GOSUMDB=off go test ./internal/server/authz/engine/rego -run '^TestEngine_IsAuthMethodBuiltin$' -count=1`) fails with `rego_type_error: undefined function flipt.is_auth_method`. The protobuf enum defines token=1, oidc=2, kubernetes=3, github=4, jwt=5, cloud=6. OPA v0.67.0 provides `rego.RegisterBuiltin2`, which registers declarations and implementations globally for both engine paths.

Hypothesis: registering the function from a package imported by both engines will make policies compile and evaluate against these numeric codes.

Result: hypothesis confirmed. Implemented `flipt.is_auth_method` with a two-argument OPA declaration (object, string), protobuf enum constants, `k8s` alias, boolean result, and specified errors. Both local Rego and bundle engines import the registration package. Tests cover each label, mismatches, alias, missing authentication, unsupported label, and policy evaluation with numeric and protobuf authentication inputs.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/server/authz/... -count=1` passed. Earlier focused test initially failed as expected with undefined function, then passed after registration. One intermediate test run failed due to formatting of the unsupported label in the error and was corrected; a later test compilation failure due to using nil for the value-type OPA context was corrected. `git diff --check` passed.
