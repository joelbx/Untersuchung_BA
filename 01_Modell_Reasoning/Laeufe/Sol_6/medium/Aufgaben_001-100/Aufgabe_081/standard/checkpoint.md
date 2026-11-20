# Checkpoint

- Task: normalize authentication session domains, omit localhost cookie Domain, and remove one trailing slash from OIDC callback hosts.
- Located code in `internal/config/authentication.go` and `internal/server/auth/method/oidc/{http,server}.go`.
- Implemented hostname normalization via `getHostname`, localhost cookie handling for state and token cookies, and single trailing slash removal for callback hosts.
- Added focused tests in `internal/config/authentication_test.go` and `internal/server/auth/method/oidc/http_test.go`.
- Verification: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/server/auth/method/oidc` passed; `git diff --check` passed.
