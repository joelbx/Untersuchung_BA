Added startup validation for enabled GitHub authentication and each configured OIDC provider. Missing or whitespace-only credentials now return the required provider and field error; the GitHub organization scope error includes the required `github` and `scopes` context.

Updated the scope validation fixture and added coverage for each missing field. `go test ./internal/config` passes.