Updated collection manifest handling so an omitted `manifest` uses `Sentinel` and retains `build_ignore`, while explicit `manifest: {}` and `manifest: null` use the default manifest directives. The file listing also excludes symlinks that point outside the collection.

All 67 tests in `test_collection.py` passed, and `git diff --check` passed.