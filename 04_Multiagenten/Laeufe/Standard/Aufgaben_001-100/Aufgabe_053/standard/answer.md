Updated `oval.major` to return `""` for zero-length input without changing how it parses non-empty versions. Added a regression case to the existing test.

The focused test and the full `./oval` test suite pass.