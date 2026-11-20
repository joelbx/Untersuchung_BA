Implemented `storage.readOnly` as an optional backend setting, added validation for non-database storage, and updated the UI selector and header to use the configured value and show the active backend icon. Authentication bootstrap now skips database connections for all non-database backends when authentication is disabled.

Added the requested invalid object-storage fixture and a config loading case for its validation error.

Verification: `go test ./internal/config ./internal/cmd` passed, and `git diff --check` passed. UI tests and build could not run because `npm` is unavailable.