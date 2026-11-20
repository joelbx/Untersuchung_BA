Fixed the OIDC login issue. Authentication validation now stores only the hostname from `Session.Domain`; localhost state and token cookies omit the `Domain` attribute; and callback URLs remove one trailing slash from the host before adding the path.

Added focused tests. `go test ./internal/config ./internal/server/auth/method/oidc` and `git diff --check` passed.