# Checkpoint

Issue: decouple feature flag evaluation from RuleStore by adding a dedicated Evaluator interface and SQL-backed EvaluatorStorage, then route Server.Evaluate through it.

Implemented:
- Added `storage.Evaluator` and SQL-backed `EvaluatorStorage` in `storage/evaluator.go`; removed Evaluate from `RuleStore`/`RuleStorage`.
- Moved the server endpoint to `server/evaluator.go`; it validates required fields, generates missing UUIDv4 request IDs, delegates through the evaluator, and records duration.
- Evaluator loads enabled flag state, rules and constraints ordered by rank, compares typed context values with normalized operators, and selects ordered distributions using CRC32 over flag key plus entity ID and 1000 rollout buckets.
- Updated storage/server test fixtures to use the new interface.

Verification: `go test ./storage ./server` passes. The Go SQLite C source emitted its existing compiler warning about returning the address of a local variable.
