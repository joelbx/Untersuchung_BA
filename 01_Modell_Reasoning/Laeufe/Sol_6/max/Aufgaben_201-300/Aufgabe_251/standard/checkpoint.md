# Validation issue checkpoint

- Goal: make YAML validation report every failure with the exact field path and source coordinates; preserve text and JSON command output and failure exit behavior.
- Initial findings: `internal/cue/validate.go` extracts YAML, unifies with the schema, then uses the first CUE input position for each error. `ValidateFiles` drops errors without positions and writes JSON directly to stdout. The command calls `ValidateFiles` and exits on `ErrValidationFailed`.
- Implemented `Result`, `FeaturesValidator`, field paths, source positions, YAML AST fallback for missing fields, and text/JSON formatting through the supplied writer. The command now prints returned errors to stderr before exiting.
- CUE's YAML positions are consistently one column past the source key/value, so the validator subtracts one for CUE-derived source positions. Focused `go test ./internal/cue` passes with exact-coordinate tests.
- Added focused tests for multiple misspelled fields, rollout bounds, missing required fields, CUE disjunctions, malformed YAML, root document type, and text/JSON output across files.
- Final verification: `go test ./internal/cue ./cmd/flipt` and `git diff --check` pass. CLI text and JSON runs against the invalid fixture show `flags.0.rules.0.distributions.0.rollout` at line 17, column 16 with a nonzero exit and `validation failed` on stderr.
