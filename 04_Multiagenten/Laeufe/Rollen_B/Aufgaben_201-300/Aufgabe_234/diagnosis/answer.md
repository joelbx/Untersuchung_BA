The checkout already uses a unified `*sql.DB`: [db.Db()](/app/db/db.go:27) returns the shared handle, [persistence.New()](/app/persistence/persistence.go:18) accepts it, and [db.Init()](/app/db/db.go:54) uses it for migrations.

The likely remaining work is:

- Complete the SQLite connection parameters in [consts.go](/app/consts/consts.go:14) and the in-memory path in [db.go](/app/db/db.go:35). The current default has a 15000 ms busy timeout and lacks `_cache_size`, `_synchronous`, and `_txlock`.
- Keep transactions on the supplied handle in [persistence.WithTx()](/app/persistence/persistence.go:109), whose fallback currently uses the global `db.Db()`.
- Use the callback’s `tx` store in [play_tracker.go](/app/core/scrobbler/play_tracker.go:164) and [initial_setup.go](/app/server/initial_setup.go:19); both currently perform operations through the outer store, outside the transaction.

The issue text conflicts with itself: its final requirement and `DB`/`dbxBuilder` interface request restore read/write separation, while its title and first four requirements call for removing it. I treated the unified-connection direction as the likely intent. `go test ./db ./persistence` passes, so these gaps are not demonstrated failures in those tests. I made no source or test edits; this was a fault-localization pass.