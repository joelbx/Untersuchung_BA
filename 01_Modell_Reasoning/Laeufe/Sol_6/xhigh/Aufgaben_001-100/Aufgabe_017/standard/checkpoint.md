# Checkpoint

Task: Add SQL Server support to Discovery database connection diagnostics.

Status: Complete. Added SQL Server routing, a SQL Server pinger using the existing go-mssqldb driver, context cancellation for prelogin reads, error classification, and focused tests. `rg` was unavailable, so repository searches used `grep` and `find`.

Verification: `GOPROXY=off GOTOOLCHAIN=local go test ./lib/client/conntest/database ./lib/client/conntest -timeout 2m` passed. `git diff --check` passed.
