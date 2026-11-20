Moved evaluation logic from `RuleStore` into the new `Evaluator` interface and SQL backed `EvaluatorStorage`. `Server.Evaluate` now delegates through that interface. The evaluator preserves rule rank order and handles typed, case insensitive comparisons, deterministic rollout boundaries, request IDs, and response metadata.

Added focused tests for comparisons, bucket boundaries, and rule priority. `go test ./...` and `git diff --check` pass.

No delegation was used; I made and verified the changes directly.