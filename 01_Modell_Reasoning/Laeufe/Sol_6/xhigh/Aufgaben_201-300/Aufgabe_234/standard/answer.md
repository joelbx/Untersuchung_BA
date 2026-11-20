The repository already passed one `*sql.DB` to persistence and migrations. I configured its SQLite DSN with all seven requested settings, removed persistence’s fallback to the global database, and changed transaction callbacks to use their `tx` store.

The read/write interface and `dbxBuilder` requirements conflict with the stated goal of reverting that split, so I did not add them.

Tests passed: `go test ./db ./persistence ./core/scrobbler ./server`.