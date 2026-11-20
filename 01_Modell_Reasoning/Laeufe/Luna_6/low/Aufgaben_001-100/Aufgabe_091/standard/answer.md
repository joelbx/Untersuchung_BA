Implemented `isoneof` and `isnotoneof` for string and numeric constraints, including JSON type validation and the 100 item limit. Added evaluator and create request validation cases.

Verification passed: `go test ./rpc/flipt ./internal/server/evaluation` and `git diff --check`. The required checkpoint is at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).