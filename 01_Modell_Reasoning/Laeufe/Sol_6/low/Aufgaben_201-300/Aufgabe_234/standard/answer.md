The repository already used a single `*sql.DB`, so I kept that architecture and resolved the remaining gaps: the SQLite connection string now includes all requested settings, persistence transactions use the connection passed to `New()`, and scrobbler writes inside `WithTx()` use `tx`.

The request also asked to create a read/write interface and builder, which conflicts with its stated goal of removing that split. I did not add them.

`go test ./db ./persistence ./core/scrobbler` passed.