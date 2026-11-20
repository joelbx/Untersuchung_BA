Implemented the configuration loader changes.

- Added `MaxIdleConn`, `MaxOpenConn`, and `ConnMaxLifetime` to the database config and mapped the corresponding `db.*` keys in [config.go](/app/config/config.go).
- Added loading for `meta.check_for_updates` and set its default to `false`, so omitted keys preserve the required default.
- Updated config coverage and fixtures for pool values, enabled and disabled update checks, and default equality in [config_test.go](/app/config/config_test.go).

Verification: `go test ./config` and `git diff --check` passed.