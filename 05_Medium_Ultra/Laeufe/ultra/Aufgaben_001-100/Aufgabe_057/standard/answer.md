Implemented YAML-native variant attachments in [internal/ext](/app/internal/ext/exporter.go). Export now renders stored JSON as YAML maps, lists, and values; import converts YAML attachments to JSON strings and handles missing or null attachments. The [CLI import](/app/cmd/flipt/import.go) and [export](/app/cmd/flipt/export.go) commands use the new package.

Added fixtures and tests for the full entity hierarchy, nested values, nulls, and pagination. The generated export matches [export.yml](/app/internal/ext/testdata/export.yml) byte for byte. `go test ./internal/ext ./cmd/flipt` and `go test ./storage/sql` passed.

I delegated the store API review, CLI wiring, and fixture tests, then integrated and verified the patch.