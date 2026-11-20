Implemented the session domain normalization, localhost state-cookie handling, and callback URL slash fix.

Verification passed: `go test ./internal/config ./internal/server/auth/method/oidc` and `git diff --check`.