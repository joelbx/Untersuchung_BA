# Checkpoint

Completed the evaluator decoupling:

- Added `storage.Evaluator` and SQL-backed `EvaluatorStorage` in `storage/evaluator.go`.
- Moved flag checks, rank-ordered rule/constraint loading, typed case-insensitive constraint evaluation, and CRC32 rollout selection out of `RuleStorage`; removed `Evaluate` from `RuleStore`.
- Added `Server.Evaluator`, initialized it from `New`, and delegated `Server.Evaluate` from `server/evaluator.go`, including UUIDv4 generation and duration tracking.
- Migrated existing storage/server test fixtures to the new interface.

Verification: `go test ./storage ./server` passes; `git diff --check` passes. The compiler emitted the existing SQLite C warning about a possible local-address return.
