Fixed the import failure. YAML imports now use the v3 decoder, so nested metadata and variant attachments can be serialized without the conversion workaround. JSON imports skip one leading line when it starts with `#`. Tests also verify that namespace key, name, and description are restored.

The full `internal/ext` test suite passes, and `git diff --check` is clean.