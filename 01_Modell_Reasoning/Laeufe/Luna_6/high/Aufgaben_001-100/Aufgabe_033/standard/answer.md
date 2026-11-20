Implemented multi-device U2F challenges. The auth server now generates a challenge for every registered U2F device and returns them in [auth.go](/app/lib/auth/auth.go), with the first challenge embedded to preserve the legacy JSON fields. The CLI passes the full challenge list to the existing token matching logic and falls back to the legacy format in [weblogin.go](/app/lib/client/weblogin.go).

Updated the auth client and web API types to carry the new response. MFA device management was left unchanged.

Validation: `go test ./lib/web ./lib/client` passed. The first combined run hit a timing-sensitive auth test failure; a standalone `go test ./lib/auth` rerun passed. `gofmt` and `git diff --check` passed.