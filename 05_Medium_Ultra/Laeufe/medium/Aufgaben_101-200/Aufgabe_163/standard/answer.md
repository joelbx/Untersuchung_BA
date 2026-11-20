Database configuration now accepts either `db.url` or separate protocol, host or SQLite path, port, user, password, and name fields. An explicit URL takes precedence. The new `DatabaseProtocol` type validates supported engines, missing fields produce qualified errors, and Postgres and MySQL use default ports when omitted.

Connection setup and migrations now resolve the configuration through the same path and apply pool settings consistently. URL parsing and connection opening errors no longer include credentials. TLS certificate errors also name their full setting keys.

Verified with `go test ./config ./storage/db ./cmd/flipt` and `git diff --check`.