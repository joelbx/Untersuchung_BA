Implemented the OIDC fixes:

- [authentication.go](/app/internal/config/authentication.go:103) normalizes the session domain to its hostname and propagates URL parsing errors.
- [http.go](/app/internal/server/auth/method/oidc/http.go:137) omits the state cookie’s Domain attribute for `localhost`, preserving its callback path.
- [server.go](/app/internal/server/auth/method/oidc/server.go:161) removes one trailing slash before building the callback URL.

`gofmt`, `git diff --check`, and `go test ./internal/config ./internal/server/auth/method/oidc` passed. Checkpoint recorded in `.codex-role-output/checkpoint.md`.