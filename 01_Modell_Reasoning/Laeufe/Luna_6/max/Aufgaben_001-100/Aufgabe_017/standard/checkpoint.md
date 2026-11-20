# Checkpoint

Issue: add SQL Server support to Teleport Discovery database connection diagnostics.

Implemented:
- Added `SQLServerPinger` using the SQL Server TDS connector with the supplied host, port, username, and database, then a context-aware ping.
- Added validation for SQL Server parameters and error categorization for refused connections, login failures, and missing/unopenable databases.
- Registered the `sqlserver` protocol in the diagnostic pinger factory; unsupported protocols return an error.
- Added focused tests for connection success, validation, cancellation, error classification, and factory routing.

Validation: `go test ./lib/client/conntest/database ./lib/client/conntest` passed. `gofmt` and `git diff --check` passed.
