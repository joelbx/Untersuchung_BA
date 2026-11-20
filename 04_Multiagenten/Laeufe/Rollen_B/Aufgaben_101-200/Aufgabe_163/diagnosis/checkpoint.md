# Fault-localization checkpoint

Started: inspect repository database configuration, connection, and migration paths; no project source or tests will be edited.

Observed: config/config.go DatabaseConfig and Load only expose/read db.url; Default sets SQLite URL, so separate fields would be ignored unless URL precedence is handled explicitly. storage/db/db.go Open and storage/db/migrator.go NewMigrator both pass cfg.Database.URL into open. db.parse formats raw URL in parse errors, which may expose credentials.

Existing tests: go test ./config passes. config/config_test.go covers URL/default config and HTTPS certificate errors with unqualified field names; storage/db/db_test.go covers URL parsing and driver-specific DSNs, not key/value inputs. NewMigrator currently takes *config.Config while Open takes config.Config by value. MySQL and SQLite parse paths inject driver parameters; those must be preserved in both modes. Uncertainty: SQLite key mapping (db.host versus db.path) is not represented in current config and should be specified during implementation.
