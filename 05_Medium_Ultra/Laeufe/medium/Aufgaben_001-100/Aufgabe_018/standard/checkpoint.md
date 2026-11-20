Task: Fix scalar string to []string configuration decoding so whitespace separates values for YAML and ENV, including empty strings.
Status: Complete. Implemented a string-only []string whitespace hook, enabled empty ENV values in Viper, updated the advanced YAML fixture, and added YAML/ENV scalar and sequence tests. `go test ./internal/config` and `git diff --check` pass.
