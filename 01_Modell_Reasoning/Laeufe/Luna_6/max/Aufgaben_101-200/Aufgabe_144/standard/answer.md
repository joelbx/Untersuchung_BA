Implemented `expand_record()` in [catalog/utils/__init__.py](/app/openlibrary/catalog/utils/__init__.py:44), including normalized title variants, a 25 character short title, merged ISBNs, optional edition fields, and blank country filtering.

Updated add-book matching and merge documentation to use the new helper, removed the old implementation, and consolidated title building in `catalog.utils`.

Verification: 69 passed, 7 skipped, 2 expected xfails across the focused suites. `ruff check` and `git diff --check` passed. No code references to `build_marc` remain.