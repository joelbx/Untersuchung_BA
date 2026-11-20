Implemented precise YAML validation errors in [the validator](/app/internal/cue/validate.go:63). `Result.Errors` now collects multiple failures, with a field path, descriptive message, and coordinates from the original YAML. The [validate command](/app/cmd/flipt/validate.go) presents them as text or JSON and exits with a failure signal.

Added regression tests for sibling misspelled keys, an out of range rollout, output formats, and exit behavior. Offline tests passed: `go test -count=1 ./internal/cue ./cmd/flipt`. A real JSON invocation exited with code 1 and reported the rollout error at line 17, column 16.

I delegated the validator and command edits, used a separate read-only review, and verified the integrated patch.