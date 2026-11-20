Task: Add SQL Server support to connection diagnostics.
Status: Complete. Added SQLServerPinger, selector registration, and focused tests for connection, timeout, validation, and error classification.
Verification: GOPROXY=off go test ./lib/client/conntest/database ./lib/client/conntest (passed); git diff --check (passed).
Constraints: Used local code and tests only; preserved git history, index, and harness configuration.
