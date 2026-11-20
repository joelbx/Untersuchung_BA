The checked out code already used a single `*sql.DB`. I completed the remaining work: added the requested SQLite connection options, made `WithTx()` use the connection passed to `persistence.New()`, and changed two transaction callbacks to use `tx`.

The issue’s final requirement and interface section ask for separate read/write connections, which conflicts with its stated goal. I followed the unified connection behavior.

The existing tests passed for `db`, `persistence`, `core/scrobbler`, and `server`.