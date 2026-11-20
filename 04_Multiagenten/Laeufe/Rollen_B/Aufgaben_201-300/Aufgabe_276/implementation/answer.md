GitHub and enabled OIDC providers now require non-empty `client_id`, `client_secret`, and `redirect_address` values at startup. Validation errors name the provider and field; GitHub’s `read:org` scope error now uses the specified message.

I updated the scope fixture and added configuration loading tests. `go test ./internal/config -count=1` passes.