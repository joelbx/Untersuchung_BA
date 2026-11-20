# Checkpoint

Issue: JWT authentication with non-database flag storage still opens an authentication database connection.

Initial findings: `authenticationGRPC` returns early only when authentication is entirely disabled, so JWT-only configurations call `getDB`. Method metadata currently lacks a database requirement. Cleanup scheduling also ignores that requirement.

Plan: add explicit method requirements, use them for database and cleanup decisions, preserve JWT middleware on the in-memory path, and run relevant existing Go tests.

Completed: method metadata declares `RequiresDatabase` for all five methods; configuration checks enabled methods for database and cleanup needs. Authentication startup uses an in-memory store when no enabled method requires a database and still configures JWT middleware. Cleanup skips disabled and database-free methods.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/cmd ./internal/cleanup` passed. An isolated JWT startup regression test also passed for Local, Git, and OCI storage with an invalid database URL. `git diff --check` passed. The Go-generated `go.work.sum` change was restored.
