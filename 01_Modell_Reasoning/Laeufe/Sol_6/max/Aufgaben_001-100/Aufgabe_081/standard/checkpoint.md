# Checkpoint

Task: Fix OIDC session domain normalization, localhost state cookie domain, and callback URL trailing slash handling.

Status: Implemented hostname normalization in authentication validation, omitted localhost cookie domains for OIDC state and token cookies, and removed one trailing slash from callback hosts. Added regression tests and exercised the trailing-slash callback in the existing OIDC integration test.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/server/auth/method/oidc` passed.
