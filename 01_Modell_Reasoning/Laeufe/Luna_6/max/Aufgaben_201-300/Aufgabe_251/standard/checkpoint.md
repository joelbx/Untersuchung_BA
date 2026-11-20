# Checkpoint

Task: resolve imprecise and repetitive YAML validation errors in `internal/cue/validate.go` and `cmd/flipt/validate.go`.

Implemented: added `Result` and `FeaturesValidator`, with structured field paths, descriptive messages, and source locations selected from the input file's CUE positions. `ValidateFiles` aggregates diagnostics across files and writes both JSON and text output to its supplied writer.

Verification: `go test ./internal/cue` passes. CLI smoke runs for JSON and text report all four sample failures (`ey`, `nabled`, `escription`, and rollout 110) with distinct YAML line and column coordinates and exit with status 1.
