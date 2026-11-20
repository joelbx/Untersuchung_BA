GitHub and enabled OIDC providers now fail startup when `client_id`, `client_secret`, or `redirect_address` is empty. Errors identify the provider and field; GitHub’s `read:org` check also uses the required error format.

Added YAML startup regression tests and updated the GitHub scope fixture. `go test ./internal/config ./internal/cmd` and `git diff --check` passed.