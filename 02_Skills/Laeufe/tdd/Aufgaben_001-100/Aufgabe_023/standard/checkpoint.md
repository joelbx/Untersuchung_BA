# Checkpoint

Task: Fix JWT authentication startup with non-database flag storage and database-only cleanup.

Changes: Added explicit `RequiresDatabase` metadata for all authentication methods; used enabled methods to decide database initialization and cleanup; kept JWT middleware registration with an in-memory auth store; skipped cleanup for disabled and non-database methods. Added configuration, startup, and cleanup regressions.

TDD red: `GOPROXY=off go test ./internal/config ./internal/cmd -run 'TestAuthentication(DatabaseRequirements|CleanupRequiresDatabase|GRPCJWTWithoutDatabase)$' -count=1` failed because `RequiresDatabase` was absent and JWT startup attempted to open `invalid://database-should-not-be-opened`. `GOPROXY=off go test ./internal/cleanup -run '^TestCleanup$' -count=1` failed because JWT cleanup deleted its record.

Focused green: `GOPROXY=off go test ./internal/config ./internal/cmd ./internal/cleanup -run 'TestAuthentication(DatabaseRequirements|CleanupRequiresDatabase|GRPCJWTWithoutDatabase)$|^TestCleanup$' -count=1` passed.

Full suite: `GOPROXY=off go test ./...` running.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used grep/find. Go test initially modified `go.work.sum`; restored it from HEAD without changing the index.

Full suite result: `GOPROXY=off go test ./...` failed in unrelated tests requiring unavailable external services. `internal/cache/redis`: `TestSet`, `TestGet`, `TestDelete` each failed with `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?: failed to create container`. `internal/gitfs`: `Test_FS_Submodule` failed with `Get "https://github.com/flipt-io/flipt-gitops-test.git/info/refs?service=git-upload-pack": Forbidden`. All changed packages passed in that run. These service-dependent tests remain unverified in this environment.

Final relevant package run: `GOPROXY=off go test ./internal/config ./internal/cmd ./internal/cleanup -count=1` passed after final refactor. `git diff --check` passed. Restored incidental `go.work.sum` changes after the test run; index and git history untouched.
