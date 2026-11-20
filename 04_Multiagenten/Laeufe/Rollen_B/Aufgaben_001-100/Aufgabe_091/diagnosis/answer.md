The issue is localized to three files:

- [legacy_evaluator.go](/app/internal/server/evaluation/legacy_evaluator.go:312): `matchesString` has no list cases. `matchesNumber` parses the constraint value as a single float before its operator switch, so a JSON array cannot reach list matching.
- [operators.go](/app/rpc/flipt/operators.go:3): both constants and their entries in `ValidOperators`, `StringOperators`, and `NumberOperators` are missing.
- [validation.go](/app/rpc/flipt/validation.go:372): create and update validation check the operator and whether a value is present, but never check array type or the 100 item limit.

The fix should cover exact membership and absence for strings and numbers; malformed and mixed type arrays; the 100/101 item boundary; and validation errors with the specified messages. One edge case needs care: JSON `null` unmarshals successfully into a nil slice, so decoding alone does not establish that the value is an array. Date validation also reuses `NumberOperators`, which could inadvertently admit the new operators for dates.

The focused existing tests pass, but they contain no list operator cases. **No project source or tests were changed** under the assigned fault localization scope. I recorded the findings in [checkpoint.md](/app/.codex-role-output/checkpoint.md).