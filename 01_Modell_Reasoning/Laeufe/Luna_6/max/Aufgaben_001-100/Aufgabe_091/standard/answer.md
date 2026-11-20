Implemented `isoneof` and `isnotoneof` for string and numeric constraints, including strict JSON array validation and the 100 item limit. Added regression tests for matching, invalid values, wrong element types, and oversized arrays.

`GOPROXY=off go test ./rpc/flipt ./internal/server/evaluation` passed, and `git diff --check` passed.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)