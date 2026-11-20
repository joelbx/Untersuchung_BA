# Checkpoint

Implemented YAML-native variant attachment import and export in `internal/ext`, and connected the CLI commands to it. This checkout has no `internal/ext/testdata` fixtures. Tests pass: `go test ./internal/ext ./cmd/flipt` and `go test ./storage/... ./internal/ext`.
