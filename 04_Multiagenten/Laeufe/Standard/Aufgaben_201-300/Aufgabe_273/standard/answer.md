Updated `make_work` to return a work with an empty `authors` list when either author field is missing. It now preserves a supplied `cover_url`, applies the requested metadata defaults, and includes the requested type annotations.

Added regression tests. The addbook test file passes: **15 passed**.