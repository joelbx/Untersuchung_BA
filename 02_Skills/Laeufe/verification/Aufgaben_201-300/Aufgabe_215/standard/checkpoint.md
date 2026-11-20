# Checkpoint

Task: add HTTPS configuration and serving support in `/app`.

Implemented:
- `configure(path)` uses a fresh Viper instance, reads YAML, applies `FLIPT` environment overrides, overlays defaults, and validates HTTPS certificate and key paths with the specified error text.
- Added `Scheme`, server protocol/port/certificate settings, HTTPS REST/UI listener, and TLS gRPC listener. The REST gateway pins the configured gRPC certificate when using TLS.
- Updated configuration examples and documentation. Added tests for defaults, advanced YAML, environment overrides, CORS origin forms, validation errors, and metadata handlers.
- Scoped `.gitignore` binary rule to `/flipt` so the new test file appears in repository changes.

Verification executed: `GOPROXY=off GOSUMDB=off go test ./...` exited 0 on 2026-10-29; all package tests passed. `git diff --check` exited 0. The compiler emitted an existing warning in the sqlite3 C dependency. No network TLS integration test was run.

Local tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); inspection used `grep` and `find`.
