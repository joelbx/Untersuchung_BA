# Checkpoint

Task: Fix authentication database initialization for JWT with non-database storage.

Status: Fixed and verified.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep` and `find`.

Root cause: authenticationGRPC uses Authentication.Enabled() to choose DB access. JWT sets Enabled() true despite needing no persistent store. The no-DB branch returns early, bypassing JWT middleware. Cleanup scheduling also considers JWT and disabled methods without DB dependency filtering.
Hypothesis: method-level RequiresDatabase metadata, combined with a conditional DB-backed auth store and shared registration path, prevents DB initialization while preserving JWT middleware. Cleanup must use the same metadata.

Reproduction before fix:
- `go test ./internal/config ./internal/cmd -run 'TestAuthenticationDatabaseRequirements|TestAuthenticationGRPCJWTWithoutDatabase' -count=1` failed as expected: `AuthenticationConfig.RequiresDatabase` and `StaticAuthenticationMethodInfo.RequiresDatabase` were undefined; JWT startup failed with `opening db: error parsing url: invalid database scheme`.

Patch:
- Added explicit RequiresDatabase metadata for token, OIDC, GitHub, Kubernetes (true), JWT (false).
- Added AuthenticationConfig.RequiresDatabase; cleanup eligibility now checks enabled, database requirement, and configured schedule.
- Authentication gRPC startup uses an in-memory auth store for non-DB storage with no DB-dependent auth method and proceeds to register JWT middleware; DB-backed cases retain SQL auth store.
- Authentication cleanup skips disabled and database-free methods.
- Added configuration, startup, and cleanup regression tests.

Verification:
- `go test ./internal/config ./internal/cmd ./internal/cleanup -count=1` passed (all three packages).
- `git diff --check` passed.
- Go tooling changed go.work.sum during the initial test build; restored its original contents from HEAD. No external downloads were requested.
