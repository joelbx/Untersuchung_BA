# Checkpoint

Resolved YAML/JSON import metadata issue. YAML import now uses the YAML v3 decoder, JSON import skips exactly one leading line when its first byte is `#`, and variant attachments serialize directly from decoded values. Added roundtrip regression coverage for nested metadata, namespace key/name/description, YAML and JSON exports, and strict JSON header behavior.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/ext ./cmd/flipt` passed; `git diff --check` passed. The CLI package has no test files.
