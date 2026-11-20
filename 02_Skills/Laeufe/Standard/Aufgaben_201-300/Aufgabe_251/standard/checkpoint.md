# Checkpoint

Task complete: improved YAML diagnostics for `flipt validate`.

Changes:
- Added `Result`, `FeaturesValidator`, `NewFeaturesValidator`, and structured `Validate` API.
- Collects all CUE validation errors with field paths and descriptive messages. Positions come from the original YAML source: unknown keys point at the key; invalid values point at the value.
- Text and JSON output aggregate errors. CLI reports validation failure on stderr and exits with its configured issue code.
- Added tests for misspelled keys, range constraints, exact coordinates, output formats, and multiple files.

Checks:
- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/cue ./cmd/flipt`: passed (`cmd/flipt` has no test files, package compiled).
- `git diff --check`: passed.
- `rg` unavailable (`/bin/bash: rg: command not found`); used local `grep` and `find`.
