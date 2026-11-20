# Checkpoint

Task: restore whitespace splitting for scalar string values decoded into `[]string` in configuration, including YAML and ENV.
Status: complete.
Changes: replaced comma splitting with a string-to-`[]string` decode hook using `strings.Fields`; updated the advanced CORS fixture and added focused YAML, ENV, empty-input, sequence, and hook type-guard coverage.
Verification: `GOPROXY=off go test ./internal/config` passed; `git diff --check` passed.
