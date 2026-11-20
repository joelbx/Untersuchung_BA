# Checkpoint

Task: Add `isoneof` and `isnotoneof` operators for string and numeric constraints, validate JSON arrays, and enforce a 100-item maximum.

Implementation complete:
- Added the operators to the public constants and string/number operator maps.
- Added string and numeric list matching in the legacy evaluator.
- Added strict JSON array type validation and the public 100-item limit constant to constraint request validation.
- Added regression coverage for both operators, invalid values, wrong element types, and item limits.

Verification: `GOPROXY=off go test ./rpc/flipt ./internal/server/evaluation` passed. `git diff --check` passed.
