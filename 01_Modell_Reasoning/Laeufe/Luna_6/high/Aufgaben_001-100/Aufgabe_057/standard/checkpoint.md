# Checkpoint

Implemented the `internal/ext` YAML document types, exporter, and importer.

- Export translates stored JSON attachments to YAML-native values and preserves explicit top-level JSON null.
- Import recursively normalizes YAML map keys and stores attachments as JSON strings.
- Flags, variants, segments, constraints, rules, and distributions are handled through the store interfaces.

Verification completed: `go test ./internal/ext ./cmd/flipt` and `go test ./storage/sql ./storage/cache` pass. `git diff --check` passes.
