Implemented the dedicated `Evaluator` interface and SQL-backed `EvaluatorStorage` in [storage/evaluator.go](/app/storage/evaluator.go). Evaluation is removed from `RuleStore`, and [server/evaluator.go](/app/server/evaluator.go) validates requests, supplies missing UUIDv4 request IDs, delegates evaluation, and records duration.

The evaluator handles typed, case-insensitive constraints, deterministic CRC32 rollout selection, and the required response fields and flag errors. Updated the existing test fixtures for the new interface.

**Verification:** `go test ./storage ./server` passes. `git diff --check` is clean.