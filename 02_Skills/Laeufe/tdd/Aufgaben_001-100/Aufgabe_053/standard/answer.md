Updated [oval/util.go](/app/oval/util.go:280) so `major("")` returns `""` without panicking. Non-empty parsing behavior is unchanged. Added a [regression test](/app/oval/util_test.go:1116) that failed with the original slice panic before the fix.

`GOPROXY=off GOSUMDB=off go test ./...` passed. The build emitted a `go-sqlite3` C compiler warning.