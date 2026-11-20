Implemented the import fix. YAML now uses v3, JSON import skips one initial line only when it starts with `#`, and nested metadata and attachments are serialized directly. Added regression coverage for nested data and namespace fields.

`go test ./internal/ext` and `git diff --check` passed. Updated `.codex-role-output/checkpoint.md`.