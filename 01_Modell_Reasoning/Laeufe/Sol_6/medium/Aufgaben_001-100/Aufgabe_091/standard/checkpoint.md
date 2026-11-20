Task: Add isoneof and isnotoneof for string and number constraints, with JSON array validation and 100-item limit.
Status: Implemented in evaluator, operator maps, and create/update validation.
Verification: go test ./rpc/flipt ./internal/server/evaluation passed; git diff --check passed.
Files: rpc/flipt/operators.go, rpc/flipt/validation.go, internal/server/evaluation/legacy_evaluator.go, and focused tests in both packages.
