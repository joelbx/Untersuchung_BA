# Checkpoint

Implemented optional storage.readOnly in Go and TypeScript, validation for non-database storage, config-based UI readonly selector, storage-aware header icons, and authentication bootstrap guard for non-database backends. Explicit readOnly is decoded even when experimental filesystem storage is disabled. Added invalid_readonly.yml plus config tests for invalid object storage and database YAML/environment values.
Verification: `go test ./internal/config ./internal/cmd` passed; `git diff --check` passed. UI dependencies are absent, so UI test/build commands were unavailable.
No delegation used.
