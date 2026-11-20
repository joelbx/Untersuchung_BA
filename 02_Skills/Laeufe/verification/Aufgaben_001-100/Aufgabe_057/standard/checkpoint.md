# Checkpoint

Implemented `internal/ext` document types, exporter, importer, and recursive YAML-map conversion. CLI import/export now call these components. Attachments export as YAML values and import as JSON strings; absent attachments remain empty. Legacy JSON-in-YAML strings are accepted.

Verification:
- `GOPROXY=off go test -count=1 ./internal/ext ./cmd/flipt ./storage/...` — exit 0; ext, cache, and SQL tests passed, other listed packages had no tests.
- `git diff --check` — exit 0.
- The issue references `internal/ext/testdata/export.yml`, `import.yml`, and `import_no_attachment.yml`, but none exist in this checkout. Focused local tests cover the same attachment and relationship cases.
