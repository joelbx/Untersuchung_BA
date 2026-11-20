Implemented the evaluator decoupling. `RuleStore` no longer includes `Evaluate`; `Server` delegates evaluation through `storage.Evaluator`, with SQL evaluation handled by [storage/evaluator.go](/app/storage/evaluator.go) and server validation, UUID generation, and duration tracking in [server/evaluator.go](/app/server/evaluator.go).

Migrated the existing test fixtures to the new interface.

Verified with `go test ./storage ./server` and `git diff --check`; both passed.