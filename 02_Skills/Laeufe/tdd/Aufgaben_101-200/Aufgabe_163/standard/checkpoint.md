# Checkpoint

Implemented separate database settings (`db.protocol`, `db.host`, `db.port`, `db.user`, `db.password`, `db.name`, `db.path`) with URL precedence. A public `DatabaseProtocol` enum distinguishes SQLite, Postgres, and MySQL. Both regular connections and migrations resolve the target through `DatabaseConfig.ConnectionURL`, which validates required values, applies default ports, and escapes URL credentials. Migrations now take `config.Config` by value. TLS validation errors use fully qualified keys. Database URL parsing and opening errors omit credentials. The sample config documents both modes.

Test-driven sequence: New config tests first failed on the default URL and missing validation; new connection tests first failed on empty URL parsing and exposed credentials; new migrator test first failed on empty URL parsing; invalid port and numeric protocol tests first failed on missing validation/value reporting. Implementations followed each failure.

Verification:
- `go test ./config ./storage/db -count=1` passed.
- `go test ./...` passed across all packages.
- `git diff --check` passed.
- The Go build emits a compiler warning from `github.com/mattn/go-sqlite3` C source (`sqlite3-binding.c`, `-Wreturn-local-addr`); tests still pass.

Environment: `rg` unavailable (`/bin/bash: rg: command not found`); local `grep`/`find` used. No downloads performed.
