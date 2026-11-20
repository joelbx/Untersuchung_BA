# Checkpoint

Implemented startup validation for enabled GitHub authentication and each configured OIDC provider. Required client_id, client_secret, and redirect_address values must contain non-whitespace text. Errors name the provider and field. GitHub allowed_organizations still requires read:org, with the requested provider-qualified error.

Updated the existing scope fixture and added load-time regression cases for missing fields and the exact OIDC YAML provider key. `go test ./internal/config -count=1` passes. `git diff --check` passes.
