Fixed the import issue. YAML imports now use the v3 decoder, preserving nested metadata and allowing variant attachments to serialize directly to JSON. JSON imports accept one leading line starting with `#`. Tests also verify that namespace key, name, and description are applied.

`go test ./internal/ext` passed. `go test ./cmd/flipt` completed; that package has no test files.