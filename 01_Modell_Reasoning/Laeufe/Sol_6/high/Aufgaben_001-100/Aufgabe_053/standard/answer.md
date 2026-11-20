Added an empty-input guard so `oval.major("")` returns `""` without panicking. The existing parsing path for non-empty inputs is unchanged. Added a regression case in [oval/util_test.go](/app/oval/util_test.go:1094).

`GOPROXY=off GOSUMDB=off go test ./oval` and `git diff --check` passed.