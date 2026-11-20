# Checkpoint

Task: validate required GitHub and OIDC authentication fields during configuration loading, with provider-specific error messages and the GitHub organization scope rule.

Findings: `internal/config/authentication.go` already calls method validation for enabled authentication methods, but OIDC validation is empty and GitHub validation only checks `read:org` with an unqualified error. Existing configuration tests cover the GitHub scope rule.

Completed: added non-empty checks for enabled GitHub and every configured enabled OIDC provider, with field and provider names in errors. GitHub organization scope errors now use the required wording. Method validation runs before session-domain validation so missing provider credentials surface with their provider-specific error.

Verification: `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./internal/config` passed after the final test update. The load-path tests cover missing and whitespace-only fields, a second invalid OIDC provider, valid configurations, disabled methods, and the existing GitHub organization scope rule.
