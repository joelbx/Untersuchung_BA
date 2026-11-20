# Checkpoint

Completed SQL Server support for connection diagnostics:

- Protocol dispatch returns `SQLServerPinger` for `sqlserver`; unknown protocols still return the existing unsupported-protocol error.
- The new pinger validates required parameters, uses the SQL Server driver with `PingContext`, and categorizes refused connections, failed logins, and invalid database names.

Verification passed: `go test ./lib/client/conntest/database ./lib/client/conntest`.
