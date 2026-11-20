Implemented support for database URLs and discrete SQLite, Postgres, and MySQL settings. URLs retain precedence; discrete settings are validated, default engine ports, and are converted to driver-specific targets internally. Passwords are redacted from connection errors and JSON output.

Migration setup now accepts `config.Config` by value and applies the same connection and pool configuration. Validation errors identify fully qualified database and TLS settings.

Verification passed: `GOPROXY=off go test ./config ./storage/db ./cmd/flipt`. `git diff --check` passed.