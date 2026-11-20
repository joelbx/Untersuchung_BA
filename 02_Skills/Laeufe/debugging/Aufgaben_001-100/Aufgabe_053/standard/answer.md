Fixed `oval.major("")` so it returns `""` normally. The change in [oval/util.go](/app/oval/util.go:280) leaves the parsing path for non-empty inputs unchanged, and [oval/util_test.go](/app/oval/util_test.go:1094) now covers empty input.

The new test reproduced the original panic before the fix. Afterward, the focused test and the full `oval` package tests passed.