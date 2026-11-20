Updated authentication validation to store only the hostname in `Session.Domain` and propagate URL parsing errors. OIDC state and token cookies now omit `Domain` for localhost, and callback URLs remove one trailing slash from the host before adding the callback path.

Verification passed: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/server/auth/method/oidc` and `git diff --check`.