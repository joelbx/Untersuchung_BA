# Checkpoint

Implemented `storage.readOnly` as an optional backend config field with database-only validation, added the requested invalid object-storage fixture, skipped database auth bootstrap for all non-database storage backends when auth is disabled, exposed `selectConfig`, derived readonly state from config with storage defaults, and added storage-specific header icons alongside the Read-Only badge.

Validation: `go test ./internal/config` passed. `go test ./internal/cmd` is still running. UI test execution is unavailable because `npm` is not installed in the environment.
