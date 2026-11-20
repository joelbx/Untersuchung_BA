The repository already uses a single `*sql.DB` for persistence, so I left that architecture in place and added the requested SQLite connection parameters in [db.go](/app/db/db.go).

Existing tests passed: `go test ./db ./persistence`.