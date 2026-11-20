Updated [make_work](/app/openlibrary/plugins/upstream/addbook.py:69) to return a `web.Storage` when either author field is missing, with an empty `authors` list. It now preserves a supplied cover URL and applies the requested metadata defaults. I also added the requested type annotations and regression tests.

Verification: all 15 tests in `test_addbook.py` passed, and `git diff --check` passed.