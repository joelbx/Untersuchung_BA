Updated `oval.major` to return `""` for empty input and added a regression test. Existing parsing behavior for non-empty input is unchanged.

Verified with `go test ./oval -count=1`.