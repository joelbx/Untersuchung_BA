Implemented startup validation for enabled GitHub authentication and each configured OIDC provider. Missing or blank `client_id`, `client_secret`, and `redirect_address` now return the required provider and field error. GitHub’s `read:org` check remains in place with the specified error text. OIDC errors preserve the provider key’s YAML spelling.

Added load tests for the required fields, disabled methods, multiple OIDC providers, and a mixed-case provider key. Tests passed for `internal/config`, `internal/cmd`, and both GitHub and OIDC auth method packages with module fetching disabled.

Two subagents reviewed the validation path and tests, then contributed the tests and YAML key preservation. I integrated and verified the final patch.