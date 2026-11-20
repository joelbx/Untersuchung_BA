Moved edition expansion to `openlibrary.catalog.utils.expand_record`, moved its title helper, removed `build_marc`, and updated the callers, documentation, and tests.

Verification: the catalog add-book and merge suites reported **85 passed, 8 skipped, 2 expected failures**. Ruff and `git diff --check` passed.