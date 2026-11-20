Implemented SQL Server connection diagnostics. `getDatabaseConnTester` now selects `SQLServerPinger` for the SQL Server protocol, and the pinger validates parameters, uses context-aware connection testing, and classifies refused connections, login failures, and invalid database names.

Verification passed: `go test ./lib/client/conntest/database ./lib/client/conntest` and `git diff --check`.