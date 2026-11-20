Configured `db.Db()` with the required SQLite connection options. The checked-out code already uses a single `*sql.DB` for persistence and migrations, so no read/write split needed removal.

`go test ./db ./persistence` passed.