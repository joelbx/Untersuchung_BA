# Database configuration issue checkpoint

Status: implemented and verified.

Changes: added DatabaseProtocol and separate db.protocol/host/port/user/password/name fields; explicit URL precedence; field-qualified validation; internal URL generation with PostgreSQL/MySQL default ports; shared connection setup for Open and by-value NewMigrator; credential-safe parse and connection errors; updated TLS field names; documented alternative configuration; added focused tests.

Checks: `go test ./...` passed after implementation. After adding a final migrator regression test, `go test ./storage/db ./config` passed. `git diff --check` passed. The C compiler emitted an existing sqlite3 warning but tests passed.
