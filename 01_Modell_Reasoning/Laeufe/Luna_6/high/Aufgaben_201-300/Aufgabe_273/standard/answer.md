Updated [addbook.py](/app/openlibrary/plugins/upstream/addbook.py:69) so `make_work()` handles missing author fields, creates authors from matching key/name pairs, and applies defaults while preserving supplied metadata.

The existing addbook tests passed: **11 passed**. `git diff --check` was clean.