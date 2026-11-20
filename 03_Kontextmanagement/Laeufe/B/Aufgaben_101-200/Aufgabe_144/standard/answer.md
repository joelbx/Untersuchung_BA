Moved the edition expansion logic to [catalog/utils/__init__.py](/app/openlibrary/catalog/utils/__init__.py) as `expand_record()`, removed `build_marc()`, and updated callers, comments, and tests.

Validation passed: 85 tests passed, 8 skipped, and 2 expected failures. Ruff and the scoped type check passed.