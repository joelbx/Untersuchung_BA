Implemented the import fix.

- YAML imports now use yaml.v3, including updated namespace and segment decoders. Nested metadata and attachment maps can be handled as JSON compatible values without ad hoc conversion.
- JSON imports skip one initial line only when it begins with `#`.
- Namespace object fields continue through the import path so flags use the specified namespace.

`go test ./internal/ext` and `git diff --check` passed.

Changed [encoding.go](/app/internal/ext/encoding.go), [common.go](/app/internal/ext/common.go), and [importer.go](/app/internal/ext/importer.go).