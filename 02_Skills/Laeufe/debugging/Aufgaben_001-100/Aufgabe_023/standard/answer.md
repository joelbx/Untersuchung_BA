Fixed authentication startup so JWT with Local, Git, or OCI flag storage does not open a database. Each authentication method now declares whether it requires a database; startup and cleanup use that setting. JWT middleware still initializes on the database-free path.

The regression tests and existing tests passed: `go test ./internal/config ./internal/cmd ./internal/cleanup -count=1`.