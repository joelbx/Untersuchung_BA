Updated [addbook.py](/app/openlibrary/plugins/upstream/addbook.py:69): `make_author` now has the requested types and returns the created author; `make_work` handles missing author lists and preserves supplied metadata while filling absent defaults.

Validation: `pytest -q openlibrary/plugins/upstream/tests/test_addbook.py` passed (11 tests). `git diff --check` passed.