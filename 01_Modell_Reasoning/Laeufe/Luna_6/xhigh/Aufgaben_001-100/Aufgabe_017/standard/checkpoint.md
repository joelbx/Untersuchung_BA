# Checkpoint

Issue: Add SQL Server support to Teleport Discovery database connection diagnostics.

Completed: Added SQL Server protocol dispatch and SQLServerPinger using the existing go-mssqldb connector. It validates required connection fields and port range, runs PingContext with the provided context, and categorizes refused connections, authentication failures, and missing databases. Unsupported protocols retain the existing NotImplemented error.

Verification: `go test ./lib/client/conntest/database ./lib/client/conntest` passed. `gofmt` and `git diff --check` completed cleanly.
