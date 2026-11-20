Fixed [oval.major](/app/oval/util.go:280) to return `""` for empty input while leaving non-empty parsing unchanged. Added a regression case in [util_test.go](/app/oval/util_test.go:1094).

Verified with the focused test and `go test ./oval ./report`; all passed.