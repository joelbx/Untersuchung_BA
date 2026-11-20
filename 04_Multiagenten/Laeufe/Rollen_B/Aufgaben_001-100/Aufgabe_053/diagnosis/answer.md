The fault is in [oval/util.go](/app/oval/util.go:280): `major` uses `strings.Index(ver, ".")` as a slice boundary. For `""`, the index is `-1`, so the function panics instead of returning `""`.

The likely fix is an early return for zero-length input, leaving parsing of non-empty strings unchanged. [Test_major](/app/oval/util_test.go:1094) covers only dotted versions; it needs an empty-input case. The existing focused test passes, but it does not exercise the fault. This diagnosis also relies on the slice behavior rather than a new reproducing test.

I recorded the findings in `.codex-role-output/checkpoint.md`. Source and tests remain unedited because this pass was restricted to fault localization.