Added SQL Server connection diagnostics to the database pinger factory. The new `SQLServerPinger` validates connection parameters, connects within the supplied context, and categorizes refused connections, invalid users, and invalid database names.

Verification: `go test ./lib/client/conntest/database ./lib/client/conntest` passed, and `git diff --check` found no whitespace errors.