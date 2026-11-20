# Checkpoint

Implemented the database protocol enum and config fields for SQLite, Postgres, and MySQL. Config loading honors URL precedence, validates discrete inputs with fully qualified errors, applies standard ports, and keeps passwords out of JSON and connection-related errors. Connection construction, pool settings, and migration setup use the same mode. `NewMigrator` takes `config.Config` by value. TLS validation errors now name `server.cert_file` and `server.cert_key`.

Verification: `GOPROXY=off go test ./config ./storage/db ./cmd/flipt` passed. `git diff --check` passed. SQLite emitted its existing C compiler warning during compilation.
