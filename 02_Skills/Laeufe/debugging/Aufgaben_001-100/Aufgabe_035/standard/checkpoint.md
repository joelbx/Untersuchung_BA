# Checkpoint

Task: Decouple evaluation from RuleStore using EvaluatorStorage.
Status: complete.

Investigation: RuleStorage.Evaluate owned flag lookup, constraint matching, and distribution choice. It read ranked SQL rows into a Go map, losing rank order. String comparison dispatched on original operator casing even though validation lowercased it. A focused `Test_matchesString/case_insensitive_operator_and_trimmed_strings` failed before the fix with expected `true`, actual `false`.

Pattern: Rule and segment storage use SQL builders. Existing evaluation tests define distribution creation order and the server test used a RuleStore mock solely to provide Evaluate. The new EvaluatorStorage owns evaluation; Server.Evaluate delegates through an Evaluator field, with a separate mock in tests.

Changes: Move evaluation types and logic to storage/evaluator.go; remove Evaluate from RuleStore; preserve rule rank in a slice; normalize operators, trim strings, and select the first cumulative bucket cutoff at or above the CRC32 bucket; generate request IDs for direct storage evaluation. Add tests for rank and bucket boundary. Existing validation at the server boundary and UUID generation remain in server/evaluator.go.

Checks: `GOPROXY=off go test ./... -count=1` passed. `git diff --check` passed. The bundled sqlite3 C code emits a compiler warning (`sqlite3SelectNew`: function may return address of local variable), but tests pass. `rg` is unavailable (`/bin/bash: rg: command not found`), so local inspection used `grep` and `find`. No dependencies downloaded.
