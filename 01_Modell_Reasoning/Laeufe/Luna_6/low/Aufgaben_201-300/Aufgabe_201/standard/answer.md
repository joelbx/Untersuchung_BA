Implemented support for string and structured rule segments. Import and snapshot handling normalize one-key segments to OR, while export writes the canonical object form. Updated the requested fixtures and added YAML format tests.

Verification passed: `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql/...` and `git diff --check`.

SQL persistence continues to use the existing protobuf key/operator representation; its tests pass. The checkpoint is in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).