Implemented separate database credential fields with URL precedence, protocol validation, required field checks, SQLite path support, and PostgreSQL/MySQL port defaults. Connection targets are built internally, pool settings are shared with migrations, and passwords are omitted from serialized config and redacted from connection errors.

`NewMigrator` now accepts the full config by value. TLS errors identify their qualified settings. The commented config example is in [default.yml](/app/config/default.yml:25); implementation is in [config.go](/app/config/config.go:73) and [db.go](/app/storage/db/db.go:22).

Verification passed: `go test ./config ./storage/db ./cmd/flipt`. The SQLite dependency emitted a compiler warning during the run.