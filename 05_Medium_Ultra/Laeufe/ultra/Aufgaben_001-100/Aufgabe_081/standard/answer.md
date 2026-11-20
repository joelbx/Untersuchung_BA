Fixed the OIDC login issue. [Config validation](/app/internal/config/authentication.go:84) now stores only the hostname from the session domain and propagates URL parsing errors. [OIDC cookies](/app/internal/server/auth/method/oidc/http.go:59) omit `Domain` for localhost, and [callback construction](/app/internal/server/auth/method/oidc/server.go:160) removes one trailing slash while preserving the scheme and port.

Two native agents handled the config and OIDC edits; I reviewed the combined patch. The existing OIDC login test now exercises a trailing slash, and the relevant tests passed:

`GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./internal/config ./internal/server/auth/method/oidc ./internal/server/auth`