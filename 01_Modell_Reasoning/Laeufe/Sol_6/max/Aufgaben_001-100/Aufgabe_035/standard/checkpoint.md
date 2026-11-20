# Checkpoint

- Task: decouple flag evaluation from `RuleStore` into a dedicated `Evaluator` and update the server wiring.
- Initial state: working tree clean; evaluation currently lives in `storage/rule.go` and `server/rule.go`.
- Implemented: moved evaluation into `storage.EvaluatorStorage`; removed evaluation from `RuleStore`; wired `Server.Evaluate` to `storage.Evaluator`.
- Behavior: rank-ordered rules, typed and case-insensitive operators, trimmed strings, decimal/boolean parsing, CRC32 rollout boundaries, UUIDv4 request IDs, UTC timestamps, and structured flag errors.
- Verification: `GOPROXY=off GOSUMDB=off go test ./storage ./server` and `GOPROXY=off GOSUMDB=off go test ./...` passed; `git diff --check` passed.
