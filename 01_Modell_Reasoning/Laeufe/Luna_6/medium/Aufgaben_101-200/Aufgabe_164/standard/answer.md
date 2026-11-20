Fixed import decoding in `internal/ext`:

- YAML imports now use yaml.v3, preserving nested metadata as JSON-compatible maps and arrays.
- JSON imports ignore one initial line only when its first character is `#`.
- Attachments are marshaled directly, removing the conversion needed for yaml.v2 map types.
- Namespace key, name, and description decoding remains supported.

`go test ./internal/ext` passes.