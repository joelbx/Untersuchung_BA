Resolved edition matching in the checked-out files. `editions_match` now expands raw records before scoring; expansion combines ISBN variants, derives title fields, and handles missing author data. I added regression tests for matching without ISBNs and for missing titles.

Verification: 75 tests passed, 2 had expected failures. `ruff check` and `git diff --check` passed.