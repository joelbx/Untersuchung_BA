Added SQL Server support to the database connection diagnostic flow. The new pinger validates connection parameters, respects context timeouts during login, and categorizes unreachable servers, login failures, and invalid database names. Unsupported protocols still return an error.

Both relevant test packages pass: `go test ./lib/client/conntest/database ./lib/client/conntest -count=1`.