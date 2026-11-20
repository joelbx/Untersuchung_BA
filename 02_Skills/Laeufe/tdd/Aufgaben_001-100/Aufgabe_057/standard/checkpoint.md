# Checkpoint

Implemented `internal/ext` document, exporter, and importer; routed CLI import/export through them. Variant attachments export as YAML-native values and import as JSON strings. Empty attachments remain empty.

TDD: added `internal/ext/ext_test.go` first. Initial `go test ./internal/ext` failed to build because `lister`, `creator`, `NewExporter`, and `NewImporter` were absent; after implementation it passed. `go test ./internal/ext ./cmd/flipt` and `go test ./...` passed.

The issue references `internal/ext/testdata/export.yml`, `import.yml`, and `import_no_attachment.yml`, but none exist in this checkout. Exact fixture byte comparison is therefore unavailable; tests assert parsed YAML and import results.

No dependencies downloaded or git history/index/harness changed.
