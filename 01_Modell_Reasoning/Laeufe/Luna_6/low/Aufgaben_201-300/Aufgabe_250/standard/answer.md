Implemented `luqum_replace_child` with support for `BaseOperation`, `Group`, and `Unary` parents. It preserves the children sequence type and order, replaces matching children, leaves the parent unchanged if there’s no match, and raises the specified `ValueError` for unsupported parents.

Added focused tests. The query utility test file passes: **9 passed**. `git diff --check` is clean.