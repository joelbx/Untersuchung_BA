# Checkpoint

Implemented the config API requested by the issue:
- Exported `DecodeHooks`; `Load` composes its decoder from that exported slice.
- Added `DefaultConfig()` with the canonical defaults and added the missing `version` mapstructure tag.
- Changed `StorageConfig.Local` and `.Git` to pointers, retaining pointer `BasicAuth` fields, and guarded nil storage configs in validation and command use.
- Updated config tests to use the public default constructor and pointer storage values.

Verification: `go test ./internal/config ./internal/cmd` passed. `git diff --check` passed.
