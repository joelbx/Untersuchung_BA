Implemented precise YAML validation reporting in [validate.go](/app/internal/cue/validate.go). Validation results now include each error’s field path, descriptive message, and source file coordinates, and file validation collects errors across inputs.

Updated [cmd/flipt/validate.go](/app/cmd/flipt/validate.go) to use Cobra’s output writer. JSON output now goes to the requested writer as well.

Verification: `go test ./internal/cue ./cmd/flipt` and `git diff --check` passed.