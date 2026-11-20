Moved edition expansion to `catalog.utils.expand_record()`, moved its title helper alongside it, and updated the matching callers, documentation, and tests. The deprecated `build_marc()` function is removed.

The merge and add-book test suites passed: **84 passed, 8 skipped, 2 expected failures**.