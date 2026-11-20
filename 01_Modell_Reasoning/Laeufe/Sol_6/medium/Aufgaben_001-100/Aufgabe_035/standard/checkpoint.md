Task: Decouple evaluation from RuleStore into EvaluatorStorage.
Status: complete. Added Evaluator interface and SQL implementation, wired Server, moved evaluation tests to dedicated dependency, added edge case tests.
Verification: go test ./storage ./server; go test ./...; git diff --check all pass.
