Fixed the OIDC login issues. Validation now stores only the hostname in `Session.Domain`; the state cookie omits `Domain` for `localhost`; and callback URLs remove one trailing slash from the host before adding the path.

The existing tests pass: `go test ./internal/config ./internal/server/auth/method/oidc`.