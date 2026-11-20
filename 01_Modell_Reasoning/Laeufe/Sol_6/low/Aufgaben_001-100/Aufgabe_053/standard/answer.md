Updated [oval.major](/app/oval/util.go:280) to return `""` immediately for zero-length input, without changing its parsing path for non-empty strings. Added an empty-input regression case in [util_test.go](/app/oval/util_test.go:1094).

The targeted test and the full `oval` test suite pass.