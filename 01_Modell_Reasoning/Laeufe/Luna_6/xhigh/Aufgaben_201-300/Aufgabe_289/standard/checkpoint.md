# Checkpoint

Task: restore the public default configuration and decode hooks, align storage pointer types/tags, and make the default configuration pass the existing CUE schema test.

Completed: exported `DecodeHooks`; added `DefaultConfig`; added the `version` mapstructure tag; changed `StorageConfig.Local` and `.Git` to pointers; made selected-storage validation nil-safe; updated existing test fixtures for pointer fields; and made `Load` compose hooks from a copy of the exported slice plus its experimental-field hook.

Verification: `go test ./internal/config ./internal/cmd` passes; `git diff --check` passes. No `schema_test.go` is present in this checkout.
