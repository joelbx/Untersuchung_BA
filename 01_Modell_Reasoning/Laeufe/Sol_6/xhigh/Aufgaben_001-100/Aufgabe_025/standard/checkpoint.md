# Checkpoint

Task: add `${VARIABLE_NAME}` substitution to YAML configuration decoding before existing decode hooks, preserving unmatched values and existing environment overrides.

Status: implementation and tests complete. `GOPROXY=off go test ./internal/config ./config` passed; `git diff --check` passed. Restored the test-generated `go.work.sum` change.
