Task: Add SQL Server support to Teleport Discovery connection diagnostics.
Status: Complete. Added SQLServerPinger, protocol routing, error categorization, parameter validation, and tests.
Verification: go test ./lib/client/conntest/database ./lib/client/conntest -count=1 passed; git diff --check passed.
Delegation: None; coordinator implemented the solution directly.
