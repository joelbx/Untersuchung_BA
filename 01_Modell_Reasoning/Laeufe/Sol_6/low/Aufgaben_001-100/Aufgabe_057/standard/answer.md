Implemented YAML-native variant attachments in the new `internal/ext` import and export package and wired the CLI commands to use it. Export converts stored JSON into YAML structures; import converts YAML attachments into JSON strings while preserving existing JSON object and array strings.

Verified with `go test ./internal/ext ./cmd/flipt` and `git diff --check`.