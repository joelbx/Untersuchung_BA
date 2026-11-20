Updated the import flow in `/app` to decode YAML with v3, preserve nested metadata and attachments, and retain namespace key, name, and description. JSON import now skips exactly one leading line when it starts with `#`.

Verification passed: `go test ./internal/ext`, `go test ./cmd/flipt` (compilation; no test files), and `git diff --check`.