# Checkpoint

Task: support database configuration through either a URL or discrete protocol/host/port/user/password/name fields, with explicit validation, URL precedence, safe error redaction, and consistent runtime/migration behavior.

Implemented:
- Added public `config.DatabaseProtocol` (`uint8`) with SQLite, Postgres, and MySQL enum values and string parsing.
- Added URL and discrete database settings, including SQLite path support, validation for missing/invalid fields, port range validation, and engine-specific default ports.
- Configuration loading gives an explicit URL precedence and selects key/value mode when no URL is supplied. Passwords are excluded from JSON output.
- Centralized connection target construction and applied pool settings in both runtime and migration paths. `NewMigrator` now accepts the application config by value.
- Replaced URL/DSN-bearing parse errors with qualified messages and redacted runtime/migration error text. TLS certificate errors now identify `server.cert_file` and `server.cert_key`.
- Documented the discrete configuration option in `config/default.yml`.

Verification: `go test ./config ./storage/db ./cmd/flipt` passed. `git diff --check` passed. The SQLite dependency emitted its existing compiler warning about `sqlite3SelectNew` returning an address of a local variable.
