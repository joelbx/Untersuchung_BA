Added startup validation for enabled GitHub auth and each configured OIDC provider. Missing or blank credentials now report the provider key and field; GitHub’s missing `read:org` error uses the requested message.

Added config loading tests for all six required fields and updated the GitHub scope fixture. `go test ./internal/config` and `git diff --check` passed.

- [authentication.go](/app/internal/config/authentication.go:406)
- [config_test.go](/app/internal/config/config_test.go:924)