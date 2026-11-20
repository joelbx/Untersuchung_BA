Updated [oval/util.go](/app/oval/util.go:280) so `major("")` returns `""` without panicking. Added an empty-input case to [the existing test](/app/oval/util_test.go:1094). Non-empty parsing is unchanged.

The focused test, full `oval` test suite, and `git diff --check` all passed.