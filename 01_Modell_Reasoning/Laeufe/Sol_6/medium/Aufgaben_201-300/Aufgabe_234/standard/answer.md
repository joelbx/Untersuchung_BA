The repository now uses the existing single `*sql.DB` path with the requested SQLite connection options. Persistence transactions use the connection passed to `New()`, and initial setup and play count updates use the transaction store inside `WithTx()`.

The request also specifies a read/write `db.DB` interface and `dbxBuilder`. Those conflict with the issue’s stated goal of removing read/write separation, so I did not add them.

The relevant database, persistence, server, core, and scanner tests pass.