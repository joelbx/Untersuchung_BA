Fixed the import issue. YAML now uses the v3 decoder, so nested metadata and attachments can be serialized without the map conversion. JSON import accepts one leading line when its first byte is `#`. Regression tests cover nested data, namespace restoration, plain JSON, and the header rule.

Verification passed: `go test ./internal/ext ./cmd/flipt` and `git diff --check`.