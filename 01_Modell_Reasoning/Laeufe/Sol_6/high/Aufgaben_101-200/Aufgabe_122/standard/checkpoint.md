Task: add validated storage.readOnly configuration, propagate it through UI state and header, and avoid database bootstrap for disabled authentication on non-database storage.

Status: implementation complete. StorageConfig has an optional pointer boolean and validation; config loading allows the database flag without enabling filesystem storage. Redux normalizes legacy database metadata, exports selectConfig, and derives readonly from config. Header shows backend and read-only badges with backend icons. Disabled authentication bypasses the database for all non-database backends. Added config fixtures and an object-storage authentication regression test.

Verification: `go test ./internal/config ./internal/cmd -count=1` passed after all changes. UI dependencies are absent locally, so UI test/build commands are unavailable without downloading packages.
