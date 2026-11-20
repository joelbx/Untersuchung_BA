Updated [oval/util.go](/app/oval/util.go:280) so `major("")` returns `""` without changing non-empty parsing. Added an empty-input case to the existing test in [oval/util_test.go](/app/oval/util_test.go:1094).

Both `go test ./oval` and the focused `Test_major` run stalled without producing output, so I interrupted them. The test result is unverified.