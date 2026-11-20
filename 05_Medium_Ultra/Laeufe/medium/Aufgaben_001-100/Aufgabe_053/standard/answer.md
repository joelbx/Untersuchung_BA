Updated [oval/util.go](/app/oval/util.go:280) so `major("")` returns `""` without panicking. Non-empty parsing remains unchanged, and [the existing test table](/app/oval/util_test.go:1094) now covers empty input.

The `oval` tests and `report` package build pass.