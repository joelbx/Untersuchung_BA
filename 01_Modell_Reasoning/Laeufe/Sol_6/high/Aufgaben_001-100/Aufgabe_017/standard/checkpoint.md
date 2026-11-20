# Checkpoint

Task complete: SQL Server connection diagnostics now select SQLServerPinger for the SQL Server protocol. The pinger validates connection parameters, connects through the SQL Server driver with context-aware network deadlines, and categorizes refused connections, invalid users, and invalid database names. It recognizes both native SQL Server error numbers and backend messages forwarded by the Teleport SQL Server agent.

Verification: `go test ./lib/client/conntest/database ./lib/client/conntest -count=1 -timeout=120s` passed; `git diff --check` passed.
