# Checkpoint

Task: validate required GitHub and OIDC authentication fields at startup, including GitHub organization scope, with provider-specific errors.

Changes: `internal/config/authentication.go` validates non-empty `client_id`, `client_secret`, and `redirect_address` for enabled GitHub and every configured OIDC provider. GitHub scope validation now includes the provider and field. The existing scope fixture has valid credentials. Added config-load tests for empty and omitted fields, plus direct provider tests.

Verification: Before the patch, `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/config -run 'TestLoadAuthenticationRequiredFields|TestAuthenticationProviderValidation' -count=1` failed for all six required-field cases and scope error text. After the patch and test correction, `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/config -count=1` passed. `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./cmd/flipt -count=1` passed (package has no test files). `git diff --check` passed.

Environment: `rg` is unavailable; local grep/find used. No downloads requested.
