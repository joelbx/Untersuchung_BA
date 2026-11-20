Fixed the OIDC login flow. Validation now stores only the hostname in `Session.Domain`; state and token cookies omit the `Domain` attribute for `localhost`; and callback URLs remove one trailing slash from the host before adding the path. Regression tests cover each case.

`go test ./internal/config ./internal/server/auth/method/oidc` passed.