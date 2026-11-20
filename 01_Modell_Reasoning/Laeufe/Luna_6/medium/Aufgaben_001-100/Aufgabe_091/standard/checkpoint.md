# Checkpoint

Implemented public `isoneof`/`isnotoneof` operators for string and number constraints, evaluator matching, and create/update validation for JSON arrays capped at 100 entries.

Verification: `go test ./internal/server/evaluation ./rpc/flipt` passed. `git diff --check` passed. The test invocation changed `go.work.sum`; that incidental dependency file change was restored.
