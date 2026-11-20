# Checkpoint

Task: add SQL Server database connection diagnostics and error categorization.

Implemented `SQLServerPinger` with parameter validation, context-aware connection and ping, and classification for refused connections, invalid users, and invalid database names. Routed `defaults.ProtocolSQLServer` through `getDatabaseConnTester`. Added tests for routing, successful ping, validation, canceled context, and error classification.

Verification passed: `GOPROXY=off GOSUMDB=off go test ./lib/client/conntest/database ./lib/client/conntest -count=1`.
Verification passed: `git diff --check`.
