Implemented the evaluator split. `RuleStore` no longer includes evaluation; `Server.Evaluate` delegates through `storage.Evaluator`, and SQL evaluation now lives in `EvaluatorStorage` with rank-ordered rules, typed constraints, and CRC32 rollout selection.

Validation: `go test ./...` passes, and `git diff --check` is clean. The C compiler emitted an existing SQLite warning during tests.