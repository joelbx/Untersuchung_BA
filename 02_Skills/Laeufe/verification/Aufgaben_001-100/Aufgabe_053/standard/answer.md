Updated [oval/util.go](/app/oval/util.go:280) so `major("")` returns `""` without panicking. Added the empty-input case to [oval/util_test.go](/app/oval/util_test.go:1094); the existing non-empty cases remain unchanged.

The new test reproduced the panic before the fix. After the fix, `GOPROXY=off GOSUMDB=off go test ./oval -count=1` passed.