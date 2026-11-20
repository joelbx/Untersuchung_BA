Resolved the import issue. YAML imports now use the v3 decoder, preserving nested metadata and allowing attachments to serialize to JSON without a conversion step. JSON imports accept one leading line that starts with `#`. The new tests cover metadata, namespace restoration, and the comment rule.

Validation passed: `go test ./internal/ext`, `go test ./cmd/flipt`, and `git diff --check`.