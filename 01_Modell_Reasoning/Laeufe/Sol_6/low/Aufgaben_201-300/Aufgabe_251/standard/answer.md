Updated YAML validation to return a structured `Result` containing all validation errors, with field paths and locations from the source file. Text and JSON output now include those details, and validation failures return a failure signal.

The precision regression test and existing `internal/cue` tests pass. The `cmd/flipt` test run was still in progress when this response was prepared.