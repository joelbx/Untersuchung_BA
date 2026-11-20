Implemented YAML-native attachment import/export in [internal/ext](internal/ext/common.go), and routed the CLI through the shared importer and exporter ([export](cmd/flipt/export.go:63), [import](cmd/flipt/import.go:88)).

Exports render stored JSON attachments as YAML values, preserving nested maps, lists, mixed values, and nulls. Imports normalize YAML map keys and store attachments as JSON strings; missing attachments remain empty, and legacy JSON strings remain supported.

`go test ./...` passes. CLI import/export smoke checks passed for nested attachments, nulls, missing attachments, and scalar values.