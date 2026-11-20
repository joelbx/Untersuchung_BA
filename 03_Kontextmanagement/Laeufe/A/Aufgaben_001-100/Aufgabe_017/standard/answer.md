Added SQL Server connection diagnostics. The diagnostic flow now selects `SQLServerPinger` for SQL Server, validates connection parameters, respects the request context, and categorizes connection refusal, login failure, and invalid database errors.

The relevant existing and new tests passed: `go test ./lib/client/conntest/database ./lib/client/conntest`.