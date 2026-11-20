The repository now keeps database operations on one `*sql.DB`. I added the requested SQLite connection parameters, removed persistence’s fallback to the global database during transactions, and changed the play tracker to write through its transaction store. Regression tests cover the DSN settings and transaction routing.

The issue’s final requirement and interface section call for separate read and write connections, which conflicts with its title, expected behavior, and first four requirements. I followed the single-connection direction. No delegation was used.

Tests passed: `go test ./db ./persistence ./cmd ./core/... ./server/...`, followed by `go test ./db ./persistence ./core/scrobbler` after the final change.