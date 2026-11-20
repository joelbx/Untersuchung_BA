Implemented database configuration from either `db.url` or discrete `db.protocol`, `db.host`, `db.port`, `db.user`, `db.password`, and `db.name` fields. URL takes precedence; discrete settings use SQLite paths or engine defaults of port 5432 for Postgres and 3306 for MySQL. Migration setup now takes the full config by value and uses the same connection target logic as normal database opening.

Added protocol and required-field validation, URL credential redaction in parsing errors, and tests for connection target construction and URL precedence.

Verified with `go test ./config ./storage/db ./cmd/flipt` and `git diff --check`; all passed. The SQLite C compiler emitted a warning during the run.