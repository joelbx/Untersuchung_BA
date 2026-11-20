I traced the issue to two paths:

- [config/config.go](/app/config/config.go:72) defines and loads only `db.url`. Its default SQLite URL would also take precedence over new key/value settings unless the loader explicitly selects a configuration mode. This is where `DatabaseProtocol`, field validation, qualified errors, and TLS error wording belong.
- [storage/db/db.go](/app/storage/db/db.go:18) and [storage/db/migrator.go](/app/storage/db/migrator.go:30) both pass only the URL to the connection code. They need the same internal target selection and driver formatting. `NewMigrator` currently takes a pointer, contrary to the requested by-value interface.

There is a credential exposure risk in [db.go](/app/storage/db/db.go:109): URL parse errors include the raw URL, and wrapped connection errors may include a DSN. Existing tests cover URL-based configurations but no separate fields. `go test ./config` passes.

One detail remains to define in implementation: how SQLite’s file path maps to the proposed `host` and `name` fields. I recorded the findings in [checkpoint.md](/app/.codex-role-output/checkpoint.md). Per my fault-localization assignment, I made no source or test changes; the issue remains unresolved.