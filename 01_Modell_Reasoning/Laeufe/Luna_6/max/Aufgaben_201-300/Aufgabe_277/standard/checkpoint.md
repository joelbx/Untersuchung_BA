# Checkpoint

Task: resolve rollout audit log segment information.

Implemented in `internal/server/audit/types.go`: added optional operator fields, mapped single segment keys, joined multiple keys with commas, and recorded operators for multi-segment rules and rollouts.

Validation: `go test ./internal/server/audit/...` passed; `git diff --check` passed. The final tracked diff contains only `internal/server/audit/types.go`.
