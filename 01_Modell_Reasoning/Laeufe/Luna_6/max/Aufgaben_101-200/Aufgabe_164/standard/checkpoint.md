# Checkpoint

Task: resolve import failures for exported YAML/JSON containing nested metadata or a leading JSON comment line.

Implemented:
- YAML import decoding now uses yaml.v3; the custom namespace and segment decoders use yaml.v3 nodes.
- JSON decoding skips one initial line only when its first byte is `#`.
- Removed attachment map conversion; YAML v3 string-key mappings can be serialized directly.
- Existing namespace handling continues to use the structured key for flag requests and passes namespace name/description when creating a missing namespace.

Verification: `go test ./internal/ext` passed. `git diff --check` passed.
