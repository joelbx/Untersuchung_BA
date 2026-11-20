Implemented database dependency handling for authentication methods. JWT is marked database independent; static token, OIDC, GitHub, and Kubernetes require a database. Startup now connects only when database storage is configured or an enabled auth method requires persistence. Cleanup skips database independent methods.

Updated the cleanup test to verify expired JWT entries are left alone.

Verification passed: `go test -p 1 ./internal/config ./internal/cleanup ./internal/cmd`.