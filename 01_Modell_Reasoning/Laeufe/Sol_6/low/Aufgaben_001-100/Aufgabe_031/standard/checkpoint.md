# Checkpoint
config.Load now accepts an empty path, applies defaults, and binds environment overrides.
CLI startup always uses config.Load, including when no file is present.
go test ./internal/config ./cmd/flipt passed.
