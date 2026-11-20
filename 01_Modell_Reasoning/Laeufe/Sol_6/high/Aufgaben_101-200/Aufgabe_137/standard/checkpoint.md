Task: Add configurable trace sampling ratio and propagators.
Status: Implemented defaults, validation, config loading, runtime sampling and propagators, schemas, and focused tests.
Verification: Offline tests passed for ./internal/config, ./internal/tracing, and ./internal/cmd using a temporary module file selecting cached golang.org/x versions. git diff --check passed.
Constraints: Use repository code and existing tests; do not change git history, index baseline, or harness configuration.
