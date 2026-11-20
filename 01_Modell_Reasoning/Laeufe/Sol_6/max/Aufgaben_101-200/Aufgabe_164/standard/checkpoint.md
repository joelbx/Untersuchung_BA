# Import metadata fix checkpoint

Status: implementation and regression tests complete.

Changes: YAML imports now use the v3 decoder, JSON imports skip exactly one initial `#` line, and variant attachments serialize directly to JSON. Added cases for nested metadata, namespace key/name/description, JSON with and without a header, and rejection of extra comment lines.

Verification: `go test ./internal/ext` passes with network access disabled; `go test ./cmd/flipt` builds successfully (no test files); `git diff --check` passes.
