# Checkpoint

Task: implement YAML-native variant attachment import/export in `internal/ext` and use it from the CLI.
Status: complete.

Changes:
- Added shared YAML document hierarchy, exporter, importer, and recursive YAML map-key conversion.
- Export decodes stored JSON attachments into native YAML values; import encodes YAML attachments as JSON strings and leaves missing/null attachments empty.
- CLI import/export commands now call the new package.
- Added an import/export round-trip test covering nested maps, arrays, mixed values, null, missing attachment, rules, distributions, segments, and constraints.

Verification:
- `GOPROXY=off go test ./internal/ext` passed.
- `GOPROXY=off go test ./cmd/flipt ./internal/ext ./storage/cache ./storage/sql` passed.
- `GOPROXY=off go test ./...` passed.

Repository note: `internal/ext/testdata/export.yml`, `import.yml`, and `import_no_attachment.yml` are absent from this checkout, so exact fixture comparison could not be run. `rg` is unavailable (`/bin/bash: rg: command not found`); repository inspection used `find` and `grep`.
