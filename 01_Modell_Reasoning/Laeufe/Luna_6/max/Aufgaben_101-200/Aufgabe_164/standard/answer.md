Implemented the import fix.

- YAML imports now use yaml.v3, with updated namespace and segment decoding. Nested metadata and attachments can be processed without the old map conversion.
- JSON imports skip the first line only when it begins with `#`.
- Structured namespace fields remain available to the import flow, which uses the namespace key for flags and name and description when creating a namespace.

`go test ./internal/ext` and `git diff --check` passed.