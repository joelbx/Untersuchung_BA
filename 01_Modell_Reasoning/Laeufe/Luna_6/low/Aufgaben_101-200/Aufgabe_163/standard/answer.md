Implemented separate database configuration fields and connection handling.

- Added `config.DatabaseProtocol` for SQLite, Postgres, and MySQL, plus parsing and validation of `db.protocol`.
- Added `db.host`, `db.port`, `db.user`, `db.password`, and `db.name`. URL configuration takes precedence; field-based configuration uses engine defaults for ports.
- Updated database opening and `NewMigrator` to derive the connection target from the full configuration. `NewMigrator` now accepts the config by value.
- Removed raw URL text from URL parsing errors to avoid exposing embedded credentials.

Relevant existing tests passed: `go test ./config ./storage/db ./cmd/flipt`. The SQLite C compiler emitted a warning during the run.