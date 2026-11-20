The checkout already used a single `*sql.DB`. I configured the seven requested SQLite options in [db/db.go](/app/db/db.go), made persistence transactions stay on the connection passed to `New()`, and changed scrobbling and initial setup to use the transaction store.

Added tests for the SQLite settings and an isolated database connection. The relevant db, persistence, scrobbler, server, scanner, core, and cmd tests passed.

The request’s `db.DB` and `dbxBuilder` bullets conflict with its stated goal of removing read/write separation, so I followed the single-connection goal.