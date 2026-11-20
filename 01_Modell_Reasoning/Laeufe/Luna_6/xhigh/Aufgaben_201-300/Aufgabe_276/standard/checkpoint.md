# Checkpoint

Implemented startup validation in `internal/config/authentication.go`:

- Enabled GitHub authentication now requires non-whitespace `client_id`, `client_secret`, and `redirect_address` values.
- Each configured provider under enabled OIDC authentication requires those same fields; validation reports the configured YAML provider key and sorts keys for deterministic errors.
- GitHub's allowed organization scope error now includes provider `github`, field `scopes`, and the required message.
- Authentication method validation runs before session domain validation so missing method credentials are reported directly.

Added config loading coverage for all six required fields and updated the GitHub scope fixture with valid credentials.

Verification: `go test ./internal/config` passed; `git diff --check` passed.
