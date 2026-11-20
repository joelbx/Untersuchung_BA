# Checkpoint

Task: Make authentication database initialization and cleanup depend on enabled methods' explicit database requirements.

Status: Complete. Added explicit database requirements for all authentication methods. Startup uses in-memory auth storage for JWT with non-database flag storage; cleanup selects only enabled database-backed methods. Added configuration and startup tests, and updated the existing cleanup test. `go test ./internal/config ./internal/cmd ./internal/cleanup` passed, as did an isolated JWT startup test with `GOPROXY=off`. `git diff --check` passed.
