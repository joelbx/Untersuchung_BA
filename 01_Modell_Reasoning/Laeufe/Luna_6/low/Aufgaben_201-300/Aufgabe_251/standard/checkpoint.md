# Checkpoint

Issue: improve `flipt validate` diagnostics with exact field paths, per-error YAML positions, aggregate results, and valid JSON/text output.

Initial inspection: `internal/cue/validate.go` currently flattens CUE errors to generic messages and the first input position; JSON writes to stdout instead of the provided writer. `cmd/flipt/validate.go` exits on the validation sentinel.

Plan: inspect CUE v0.5 error APIs and schema, implement structured `Result`/`FeaturesValidator` API and precise message/location extraction while preserving CLI behavior, then run existing relevant tests.
