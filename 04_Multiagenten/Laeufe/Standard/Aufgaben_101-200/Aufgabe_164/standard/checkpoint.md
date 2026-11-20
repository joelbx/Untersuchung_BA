# Checkpoint

Completed YAML v3 import decoding, JSON first-line `#` handling, and removal of attachment map conversion. Added tests for nested metadata and attachments, namespace fields, JSON with and without a header, and invalid header placement. `GOPROXY=off go test ./internal/ext` passes. `go test ./cmd/flipt` was stopped during lengthy dependency compilation; it has no package tests. `git diff --check` passes.
