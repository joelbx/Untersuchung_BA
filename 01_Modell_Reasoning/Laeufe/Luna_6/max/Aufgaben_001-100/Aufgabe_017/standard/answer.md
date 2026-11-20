Implemented SQL Server connection diagnostics with context-aware connection testing and error categorization for refused connections, login failures, and invalid databases. Registered the SQL Server pinger in the diagnostic factory; unsupported protocols still return an error.

Added coverage for pinging, parameter validation, error classification, and factory routing in [sqlserver_test.go](/app/lib/client/conntest/database/sqlserver_test.go).

Validation passed: `go test ./lib/client/conntest/database ./lib/client/conntest`.