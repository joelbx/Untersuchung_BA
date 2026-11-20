# Checkpoint

Completed the OIDC domain and callback URL fixes.

- `AuthenticationConfig.validate()` normalizes non-empty session domains using `getHostname`; malformed URL errors propagate.
- State and token cookies omit the Domain attribute for `localhost`. The state cookie remains scoped to the provider callback path.
- `callbackURL` removes one trailing slash before building the callback endpoint.

Verification: `go test ./internal/config ./internal/server/auth/method/oidc` passed. `git diff --check` passed.
