# Authentication database dependency fix

Status: resolved and verified.

Changes: authentication methods now declare `RequiresDatabase`; only enabled database-backed methods trigger an auth DB connection or cleanup. JWT uses in-memory auth storage, retains JWT middleware, and bypasses cache initialization when it has no database. Added configuration and startup regression tests; updated the cleanup test for JWT.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config ./internal/cmd ./internal/cleanup` passed after the cleanup runner fix. The initial run failed in `TestCleanup` because `Run` still scheduled JWT; that issue was fixed and the same command passed. `git diff --check` passed. Restored incidental `go.work.sum` changes made by Go tooling.

Constraint: external research is unavailable; use local code and tests only. `rg` is unavailable (`/bin/bash: rg: command not found`), so repository searches use `grep`.
