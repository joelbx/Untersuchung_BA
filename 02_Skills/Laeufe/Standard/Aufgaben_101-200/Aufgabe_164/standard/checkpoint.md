# Checkpoint

Issue: exported YAML/JSON import fails on nested metadata or a leading JSON `#` line.

Changes:
- YAML import decoder uses `gopkg.in/yaml.v3`, so nested mappings in metadata and attachments decode with string keys.
- JSON decoder skips one first line only when its first byte is `#`.
- Removed attachment map conversion; the decoded value now marshals directly to JSON.
- Added focused import tests for YAML, JSON, JSON with a header, namespace fields, nested metadata and attachments, and rejection of a second/later JSON comment line.

Checks:
- `GOPROXY=off GOSUMDB=off go test ./internal/ext` — passed.
- `git diff --check` — passed.
- `GOPROXY=off GOSUMDB=off go test ./cmd/flipt` — interrupted after extended silence (exit 130); CLI package result remains unverified. This was an additional check; the import package suite passed.

Local tooling: `rg` unavailable; used `find`/`grep` for searches. No downloads requested.
