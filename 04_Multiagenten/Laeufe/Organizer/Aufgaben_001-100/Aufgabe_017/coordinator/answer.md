Added SQL Server connection diagnostics through [SQLServerPinger](/app/lib/client/conntest/database/sqlserver.go) and wired SQL Server protocol selection into [getDatabaseConnTester](/app/lib/client/conntest/database.go:416). The pinger validates connection parameters, uses the supplied context for the login attempt, and categorizes refused connections, login failures, and invalid database names.

Added tests for connection success, an expired deadline, error categories, and protocol selection. `go test ./lib/client/conntest/database ./lib/client/conntest -count=1` and `git diff --check` passed.

No delegation was used; I implemented the changes directly.