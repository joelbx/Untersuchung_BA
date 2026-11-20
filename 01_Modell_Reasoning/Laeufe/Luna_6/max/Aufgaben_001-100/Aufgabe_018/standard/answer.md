Implemented whitespace splitting for scalar strings decoded as `[]string`, while preserving comma separation and leaving other source or target types unchanged. Blank strings decode to a non-nil empty slice.

Added YAML and ENV regression coverage, plus checks for blank input and hook type gating. `go test ./internal/config` passes, and `git diff --check` is clean.