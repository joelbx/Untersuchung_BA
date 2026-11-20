Moved edition expansion to the public `catalog.utils.expand_record()` function and moved its title helper alongside it. Updated the add-book matching callers, comments, and tests, and removed `build_marc` from `merge_marc.py`.

The catalog add-book and merge suites finished with **84 passed, 8 skipped, and 2 expected failures**. Ruff and `git diff --check` passed. No delegation was used.