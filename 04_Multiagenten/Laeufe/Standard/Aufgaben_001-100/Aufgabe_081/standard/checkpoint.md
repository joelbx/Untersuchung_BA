Task: Fix OIDC session domain normalization, localhost cookie Domain, and callback URL trailing slash.
Status: Implemented in internal/config/authentication.go and internal/server/auth/method/oidc/{http,server}.go.
Verification: gofmt completed; git diff --check passed; go test ./internal/config ./internal/server/auth/method/oidc passed.
