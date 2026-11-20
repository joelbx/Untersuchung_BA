# Checkpoint

Issue: exported YAML with nested metadata fails on import, and JSON import must accept a single leading `#` line. Namespace fields must survive import.

Plan: locate import readers and existing tests, update decoding and JSON handling, add focused coverage where useful, run relevant existing tests.

Implemented: YAML imports now use the v3 decoder. JSON imports skip one first line when it starts with `#`. Removed the nested attachment map conversion. Added import tests for nested metadata, attachment JSON, namespace fields, and JSON header boundaries.

Verification: `go test ./internal/ext` passed; `go test ./cmd/flipt` passed (no test files); `git diff --check` passed.
