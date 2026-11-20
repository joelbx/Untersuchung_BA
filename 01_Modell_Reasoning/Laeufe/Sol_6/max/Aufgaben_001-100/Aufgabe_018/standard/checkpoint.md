# Checkpoint

Task: Fix scalar string to []string configuration decoding so whitespace-separated values, including CORS allowed origins and ENV sources, produce ordered slices. Preserve non-string and sequence values.

Status: Complete.

Changes:
- Replaced comma split hook with a string-to-[]string hook using strings.Fields.
- Enabled explicitly empty ENV values so they decode as empty slices.
- Updated advanced YAML fixture and added regression coverage for YAML, ENV, empty input, mixed whitespace, sequences, and non-string hook input.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/config -count=1` passed; `git diff --check` passed.
