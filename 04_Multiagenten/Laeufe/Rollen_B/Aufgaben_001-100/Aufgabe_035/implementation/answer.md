Extracted evaluation from `RuleStore` into the new `Evaluator` interface and SQL backed [EvaluatorStorage](/app/storage/evaluator.go). [Server.Evaluate](/app/server/evaluator.go) now delegates to it.

The evaluator preserves rule rank, orders distributions deterministically, handles case-insensitive typed comparisons, uses the inclusive rollout cutoff, and returns request metadata. I migrated the existing evaluation tests and added focused regression tests.

Verification: `go test ./storage ./server` passed, and `git diff --check` was clean.