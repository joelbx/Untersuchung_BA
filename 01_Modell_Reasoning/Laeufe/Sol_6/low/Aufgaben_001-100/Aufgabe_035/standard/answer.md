Added the `Evaluator` interface and SQL-backed `EvaluatorStorage`, moved evaluation logic out of `RuleStore`, and updated `Server.Evaluate` to delegate to the new dependency. Evaluation now follows rule rank, uses the specified CRC32 bucket boundary, and handles case-insensitive operators and trimmed comparisons.

The updated storage and server tests pass: `go test ./storage ./server`.