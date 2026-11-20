# Checkpoint

Task: Add SQL Server database connection diagnostics.

Implemented `SQLServerPinger` and factory routing for SQL Server. Ping validates required parameters and TCP port range, uses the existing SQL Server driver configuration, closes the socket when the context expires during login, and categorizes refused connections, invalid users, and invalid database names. Added tests for successful login, deadline behavior, validation, classification, and protocol selection.

TDD: Initial offline focused run failed because `SQLServerPinger` was missing. The first implementation exposed a deadline failure: this driver's context only governs dialing. A further failing run exposed invalid port ranges and value-form SQL Server errors. All were corrected.

Passed: `GOPROXY=off GOSUMDB=off go test ./lib/client/conntest/... -count=1` and `git diff --check` after the final edits.

Incomplete repository-wide check: `GOPROXY=off GOSUMDB=off timeout 180s go test ./...` exited 124 after the three-minute timeout. It printed only a few packages without tests before timing out and no failing test names. The full repository suite result is unknown.

`rg` unavailable (`/bin/bash: rg: command not found`); used grep/find.
