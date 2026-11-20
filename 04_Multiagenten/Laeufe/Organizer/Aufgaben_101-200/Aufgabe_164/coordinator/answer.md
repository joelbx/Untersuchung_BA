Updated the import flow to decode YAML with v3, preserving nested metadata and allowing attachments to serialize directly to JSON. JSON import now skips one leading line only when its first character is `#`. Added tests covering nested metadata, namespace key, name and description, attachments, and the JSON header rule.

`go test ./internal/ext -count=1` passed, and `git diff --check` found no whitespace errors. The CLI package test was started but interrupted during its lengthy build, so it has no result.

No delegation was used.