Updated `oval.major` to return `""` for zero-length input without changing its parsing of non-empty strings. Added an empty-input regression case to `Test_major`.

The focused test and the full `./oval` test package pass.