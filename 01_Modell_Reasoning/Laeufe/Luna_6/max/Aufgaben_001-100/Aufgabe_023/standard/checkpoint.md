# Checkpoint

Task: Resolve the authentication database requirement issue in `/app` using repository code and existing tests only.

Initial status: Working tree was clean. No `AGENTS.md` files were found. `rg` is unavailable in this environment; use `find`/`grep` as needed.

Progress: Added `RequiresDatabase` metadata to every authentication method, `AuthenticationConfig.RequiresDatabase()`, database-aware cleanup checks, and conditional authentication DB initialization with an in-memory auth store for JWT-only configurations. Added configuration coverage and adjusted cleanup coverage to exclude methods that do not use DB state.

Validation: `GOMAXPROCS=2 go test -p 1 ./internal/config ./internal/cleanup ./internal/cmd` passed. `git diff --check` passed. Go test updated `go.work.sum` as a side effect; that unrelated change was restored.

Status: Implementation and focused validation are complete.
