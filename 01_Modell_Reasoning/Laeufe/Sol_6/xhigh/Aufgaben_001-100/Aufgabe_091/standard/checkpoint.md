# Checkpoint

Task: support `isoneof` and `isnotoneof` for string and numeric constraints.
Status: implemented and verified.
Changes: operator constants/maps; JSON list matching in the legacy evaluator; create/update validation for type, shape, nulls, and maximum 100 items; focused tests.
Tests: `GOPROXY=off GOSUMDB=off go test ./rpc/flipt ./internal/server/evaluation` passed.
Notes: generated go.work.sum changes from testing were restored. No git history, index, or harness configuration changed.
