# Checkpoint

Task: add SQL Server support to database connection diagnostics.
Status: investigating repository behavior and tests.
Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep` for local inspection.

Investigation: `TestConnection` chooses a pinger by `routeToDatabase.Protocol`; `getDatabaseConnTester` handles only Postgres and MySQL, so SQL Server is rejected before the ALPN tunnel or ping. SQL Server driver and a local `sqlserver.TestServer` already exist. The driver accepts `msdsn.Config` and a context on `Connector.Connect`; its `Conn.Ping` also accepts context. Existing pingers validate via `PingParams.CheckAndSetDefaults` and categorize errors in methods consumed by `handlePingError`.
Hypothesis: registering a SQL Server pinger that uses the local driver, validates parameters, and classifies driver/network errors will make the existing diagnostic flow work without changing its checkpoint handling.

Baseline reproduction: `GOPROXY=off GOSUMDB=off go test ./lib/client/conntest/database -run 'TestSQLServer' -count=1` failed to build with `undefined: SQLServerPinger` at sqlserver_test.go:21 and :51, as expected.
Additional reproduction: after adding the pinger, `GOPROXY=off GOSUMDB=off go test ./lib/client/conntest/database -run TestSQLServerPing -count=1` failed because a negative port was not rejected as a bad parameter. Added SQL Server-specific port range validation.
Implementation: registered `SQLServerPinger` in the diagnostic factory; used the existing SQL Server driver with context-aware connect and ping, SQL Server error numbers for login/database failures, and network error detection for refused connections.
Verification: `GOPROXY=off GOSUMDB=off go test ./lib/client/conntest/... -count=1` passed (both packages). `git diff --check` passed.
