# Checkpoint

Task: implement YAML-native variant attachment import/export in `internal/ext`.

Implemented `internal/ext` YAML document types, a batched exporter, and an importer that normalizes YAML maps and converts attachments to JSON. The CLI import/export commands now use these workflows.

Validation: `go test ./internal/ext ./cmd/flipt`, `go test ./storage/sql/...`, and `go test ./...` pass; `git diff --check` is clean. Existing checkout has no `internal/ext/testdata` fixtures or package tests.
