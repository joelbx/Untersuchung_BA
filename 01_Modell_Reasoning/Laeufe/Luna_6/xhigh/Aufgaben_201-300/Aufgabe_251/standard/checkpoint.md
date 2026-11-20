# Checkpoint

Task: fix imprecise YAML validation errors in `internal/cue/validate.go` and the `flipt validate` command.

Initial status: repository is on branch `main`; no working-tree changes were reported. `rg` is unavailable in this environment, so use `find`/`grep` to inspect files.

Plan: inspect repository guidance and existing validator/CLI tests, determine how CUE errors map to YAML source positions and paths, implement structured all-errors reporting, then run relevant existing tests.

Implementation complete:
- Added `Result`, `FeaturesValidator`, `NewFeaturesValidator`, and `(*FeaturesValidator).Validate`.
- Converted aggregated CUE errors into structured errors with field paths, descriptive messages, and positions from the original YAML source.
- Updated file validation to collect errors across files and emit JSON through the supplied writer; routed CLI output through Cobra's writer.
- Kept the existing `validate` helper behavior for compatibility with its current test.

Verification: `go test ./internal/cue ./cmd/flipt` passed; `git diff --check` passed. No tests were added.
