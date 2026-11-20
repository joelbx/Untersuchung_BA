# Import metadata issue checkpoint

Status: complete.
Changes: YAML decoding uses yaml.v3; JSON import skips one leading `#` line; nested attachments serialize directly; regression tests cover nested metadata, attachments, namespace fields, and JSON header scope.
Verification: `go test ./internal/ext` passed; `git diff --check` passed. Optional `go test ./cmd/flipt` was stopped during lengthy C compilation; package has no test files.
