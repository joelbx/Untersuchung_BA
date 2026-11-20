Authentication configuration now fails during startup validation when enabled GitHub or OIDC providers lack `client_id`, `client_secret`, or `redirect_address`. Errors name the GitHub or exact OIDC provider key in the required format. The GitHub `read:org` rule also returns the specified provider-scoped error.

The added startup load tests and the full `internal/config` test package pass.