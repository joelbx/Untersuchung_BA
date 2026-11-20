Updated [oval/util.go](/app/oval/util.go:280) so `major("")` returns `""` without panicking. Added the empty-input case to [Test_major](/app/oval/util_test.go:1094); parsing for non-empty inputs is unchanged.

`go test ./oval`, `go test ./report`, and `git diff --check` all pass.