Updated [oval/util.go](/app/oval/util.go:280) so `major("")` returns `""` without panicking. Added the empty-input case to the existing test in [oval/util_test.go](/app/oval/util_test.go:1094). Non-empty parsing is unchanged.

`GOPROXY=off GOSUMDB=off go test ./oval` passed.