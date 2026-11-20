# Checkpoint

Task: add `isoneof` and `isnotoneof` string and number constraint support, validate JSON array type and 100-item limit, and run relevant existing tests.

Status: complete. Added operator constants and type maps; implemented legacy string and number membership evaluation; added create/update JSON array validation with exact error messages and 100-item limit; added focused tests including malformed JSON, wrong types, nulls, and limit boundaries.

Verification: `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./...` in `rpc/flipt` and `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/server/evaluation` in `/app` both passed. `git diff --check` passed.
