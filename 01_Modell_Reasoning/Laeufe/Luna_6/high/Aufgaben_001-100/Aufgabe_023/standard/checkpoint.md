# Checkpoint

Implemented authentication database dependency metadata and integrated it into auth startup and cleanup.

- Static token, OIDC, GitHub, and Kubernetes declare `RequiresDatabase: true`; JWT declares `false`.
- `AuthenticationConfig.RequiresDatabase()` checks only enabled methods.
- `authenticationGRPC` uses an in-memory auth store and skips DB initialization unless a method requires persistent storage; DB-backed methods retain SQL storage, locking, and optional cache behavior.
- Cleanup startup eligibility and each cleanup worker both exclude methods without database requirements.
- Added config coverage for metadata, enabled-method aggregation, and cleanup eligibility; adjusted cleanup coverage for JWT.

Verification: `go test ./internal/config ./internal/cmd ./internal/cleanup` passed.
