# Checkpoint

Task: Validate required GitHub and OIDC authentication fields at startup, including GitHub organization scope and provider-specific errors.

Root cause: `AuthenticationConfig.validate` already invokes enabled method validators during `Load`, but `AuthenticationMethodOIDCConfig.validate` returned nil and `AuthenticationMethodGithubConfig.validate` checked only organization scope. The existing scope error omitted provider and field context.

Reproduction: Added `TestLoadAuthenticationProviderValidation` and ran `go test ./internal/config -run '^TestLoadAuthenticationProviderValidation$' -count=1` before the fix. Exit 1: seven missing/blank field cases returned nil; scope case returned the old unqualified error.

Patch: Shared required OAuth field validation, called by enabled GitHub and OIDC methods; qualified GitHub scope error; supplied credentials in existing scope fixture.

Checks: `go test ./internal/config -count=1` passed. `git diff --check` passed. Broader auth/cmd tests running.
`go test ./internal/server/auth/... ./internal/cmd/... -count=1` passed (exit 0). Final `git diff --check` passed. No checks blocked by offline tooling.
