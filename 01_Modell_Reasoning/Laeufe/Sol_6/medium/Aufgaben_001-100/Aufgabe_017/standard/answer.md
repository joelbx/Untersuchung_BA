Added SQL Server connection diagnostics. The diagnostic flow now selects `SQLServerPinger` for SQL Server, validates connection parameters, applies the context deadline during login and ping, and categorizes connection refusal, login failure, and invalid database errors.

Tests passed: `go test ./lib/client/conntest/database ./lib/client/conntest`.