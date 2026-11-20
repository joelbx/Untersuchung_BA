# Checkpoint

Task: add isoneof and isnotoneof support for string and number constraints.
Status: implementation complete.
Changes: operator constants/maps, legacy evaluator list matching, create/update JSON array validation with 100 item cap, focused tests.
Verification: GOPROXY=off GOSUMDB=off go test ./rpc/flipt ./internal/server/evaluation (passed); git diff --check (passed).
