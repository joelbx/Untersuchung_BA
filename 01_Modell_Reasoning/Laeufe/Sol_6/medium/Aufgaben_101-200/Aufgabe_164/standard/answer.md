Fixed the import path. YAML imports now use the v3 decoder, so nested metadata and attachments can be serialized without the map conversion workaround. JSON imports accept one leading line that starts with `#`. Regression tests also confirm that namespace key, name, and description are applied when creating the imported namespace.

`go test ./internal/ext` and `go test ./cmd/flipt` passed.