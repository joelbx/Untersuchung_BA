# MARC role import checkpoint

Implemented role mapping in `openlibrary/catalog/marc/parse.py`, with `$4` overriding `$e`; unrecognized roles are omitted. `new_work` now carries roles from the corresponding import author to each work author link and raises on author count mismatch. Added regression tests and updated MARC fixture expectations.

Verification:
- `pytest -q -o reruns=0 openlibrary/catalog/marc/tests/test_parse.py openlibrary/catalog/add_book/tests/test_add_book.py`: 164 passed, 3 dependency deprecation warnings.
- `pytest -q -o reruns=0 openlibrary`: 2265 passed, 9 skipped, 8 xfailed, 17 warnings.
- `ruff check openlibrary/catalog/marc/parse.py openlibrary/catalog/marc/tests/test_parse.py openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py`: passed (repository lint configuration deprecation warning).
- `git diff --check`: passed.

Full-suite limitation: `pytest -q -o reruns=0` exited 1 with 2384 passed, 21 skipped, 8 xfailed, and 77 errors. Collection of `scripts/tests/test_isbndb.py` raised `requests.exceptions.ProxyError` because `raw.githubusercontent.com` returned `Tunnel connection failed: 403 Forbidden` for the import schema. Vendor infogami collection raised `ValueError: Plugin already registered under a different name` and `KeyError: 'USER'`; infogami database tests raised setup errors, including PostgreSQL connection failures. The full suite is therefore not verified green in this environment; the openlibrary suite is green.
