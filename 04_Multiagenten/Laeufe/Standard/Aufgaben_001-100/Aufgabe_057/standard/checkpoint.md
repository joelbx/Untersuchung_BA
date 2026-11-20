Task: Implement YAML-native export and import for variant attachments in internal/ext.
Status: Implemented shared YAML hierarchy, exporter, importer, and CLI integration. Added round-trip tests for nested and missing attachments.
Verification: go test ./internal/ext, go test ./storage/... ./cmd/flipt, and git diff --check passed.
