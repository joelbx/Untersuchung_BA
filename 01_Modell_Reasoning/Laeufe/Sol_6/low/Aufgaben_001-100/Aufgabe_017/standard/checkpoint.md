# Checkpoint
Task: Add SQL Server connection testing to Teleport Discovery diagnostics.
Status: Implemented and verified.
Tests: GOMAXPROCS=2 go test -p 1 ./lib/client/conntest/database ./lib/client/conntest (passed).
