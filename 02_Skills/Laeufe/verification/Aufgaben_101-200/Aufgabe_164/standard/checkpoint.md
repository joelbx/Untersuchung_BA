# Checkpoint

Implemented YAML v3 import decoding, updated YAML node hooks for namespace and segment fields, removed the variant attachment map conversion, and added JSON import support for one leading `#` line. Added tests covering nested metadata, nested attachments, namespace key/name/description, YAML comments, and JSON header limits.

Verification:
- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/ext` — passed after final edit.
- `git diff --check` — passed after final edit.
- `GOTOOLCHAIN=local GOPROXY=off go test ./cmd/flipt` — passed (package compiled; no test files).

`rg` is unavailable (`/bin/bash: rg: command not found`); used local `grep`/`find`.
