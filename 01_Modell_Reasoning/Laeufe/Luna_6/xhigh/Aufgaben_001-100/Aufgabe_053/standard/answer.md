Updated [oval/util.go](/app/oval/util.go:280) so `major("")` returns an empty string, and added an empty input case to [Test_major](/app/oval/util_test.go:1094).

`GOPROXY=off go test ./oval` passed, and `git diff --check` passed. The build emitted a C compiler warning from `go-sqlite3`.