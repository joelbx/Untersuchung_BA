Implemented the config loader changes:

- Added `MaxIdleConn`, `MaxOpenConn`, and `ConnMaxLifetime`, loaded from the requested `db.*` keys.
- Loaded `meta.check_for_updates`; changed its default to `false`, so omitted values remain false.
- Made the configured test fixture explicitly enable update checks.

`go test ./config` passed. `go test ./cmd/flipt ./storage/db` did not finish within the available wait; `git diff --check` passed.