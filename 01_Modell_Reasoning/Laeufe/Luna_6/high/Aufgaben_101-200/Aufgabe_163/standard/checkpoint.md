# Checkpoint

Implemented database URL and discrete-field configuration support.

- Added the public `DatabaseProtocol` enum and validated protocol parsing.
- Added URL precedence, key/value validation, SQLite path handling, and engine-specific port defaults.
- Centralized connection target generation and used it in both normal opens and value-based migration setup.
- Applied pool settings to migrations and redacted URL parser/driver errors that could expose credentials.
- Updated qualified TLS certificate validation errors and added configuration examples.

Verification: `go test ./config ./storage/db ./cmd/flipt` passes; `git diff --check` passes.
