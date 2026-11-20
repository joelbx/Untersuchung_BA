# Checkpoint

Implemented explicit per-method database requirements in authentication configuration. Startup now initializes the database-backed authentication store only when database flag storage is in use or an enabled auth method requires persistence. Cleanup selection and execution both skip methods that do not require a database.

Updated the existing cleanup test to verify that expired JWT authentication entries are not removed by cleanup.

Verification: `go test -p 1 ./internal/config ./internal/cleanup ./internal/cmd` passed.
