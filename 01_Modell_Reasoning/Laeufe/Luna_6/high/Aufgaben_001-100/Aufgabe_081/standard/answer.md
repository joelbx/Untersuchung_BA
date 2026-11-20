Implemented the OIDC fixes:

- Session domains are normalized to the hostname in `validate()`; URL parse errors propagate.
- State and token cookies omit the `Domain` attribute for `localhost`. The state cookie keeps its provider callback path.
- Callback URLs remove one trailing slash from the host before appending the path.

Verification passed: `go test ./internal/config ./internal/server/auth/method/oidc` and `git diff --check`.

Changed files: [authentication.go](/app/internal/config/authentication.go), [http.go](/app/internal/server/auth/method/oidc/http.go), [server.go](/app/internal/server/auth/method/oidc/server.go).