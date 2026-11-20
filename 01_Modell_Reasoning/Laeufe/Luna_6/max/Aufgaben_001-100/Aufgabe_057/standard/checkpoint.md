# Checkpoint

Task: implement YAML-native variant attachment import/export in `internal/ext` and make the CLI use it.

Implemented:
- Added shared YAML document/entity types, a paginated store-backed exporter, and a creator-backed importer.
- Export parses stored JSON attachments into native YAML maps, sequences, scalars, and nulls; absent attachments are omitted and explicit JSON null remains `null`.
- Import accepts YAML attachments, recursively normalizes map keys, JSON-encodes values for storage, preserves legacy raw JSON strings, and leaves absent attachments empty.
- Replaced the CLI's duplicated import/export logic with the shared package.

Verification:
- `go test ./...` passes.
- Manual CLI import/export checks passed for nested mixed values, nulls, missing attachments, and scalar attachments.
- `git diff --check` passes.

Repository constraint followed: no external research, downloads, delegation, history changes, index baseline changes, or harness configuration changes.
