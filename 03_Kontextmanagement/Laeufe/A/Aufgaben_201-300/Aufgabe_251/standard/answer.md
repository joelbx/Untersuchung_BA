Updated `flipt validate` to report all schema errors with each field’s path and its position in the original YAML. Text output identifies the location and issue; JSON output contains structured errors. Validation failures return `ErrValidationFailed` and produce a failure exit signal.

The new `Result` and `FeaturesValidator` API is in [internal/cue/validate.go](/app/internal/cue/validate.go). Command error reporting is in [cmd/flipt/validate.go](/app/cmd/flipt/validate.go).

Verification: `go test ./internal/cue ./cmd/flipt -count=1` passed; `git diff --check` passed.