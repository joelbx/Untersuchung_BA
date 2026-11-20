# Import preview checkpoint

Implemented non-persistent preview through import handlers and add_book pipelines. Preview returns `preview: true`, `edits`, UUID placeholder keys, and `cover_accepted`; author and language normalization are shared with normal import. Cover uploads and Archive.org writeback are skipped in preview.

TDD: added `openlibrary/catalog/add_book/tests/test_preview.py`; observed failures for missing interfaces, unmatched path, missing matched-work author, and missing existing-author edit, and missing preview metadata on language errors before implementing each behavior. Updated one existing cover test to use an allowlisted host because the requested validation rejects the old test's disallowed host.

Verification:
- `pytest -q openlibrary/catalog/add_book/tests openlibrary/plugins/importapi/tests`: 226 passed, 5 pre-existing deprecation warnings.
- `ruff check openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/load_book.py openlibrary/catalog/add_book/tests/test_preview.py openlibrary/plugins/importapi/code.py`: passed (repository configuration deprecation warning).
- `git diff --check`: passed.
- `python -m compileall -q openlibrary/catalog/add_book openlibrary/plugins/importapi/code.py`: passed.

Repository-wide gate: `pytest -q` collected 2489 items / 4 collection errors, then was interrupted after 70 passed and 74 unrelated errors because repeated setup failures made continuation uninformative. `scripts/tests/test_isbndb.py` tries to request `https://raw.githubusercontent.com/internetarchive/openlibrary-client/master/olclient/schemata/import.schema.json` during import and fails with `ProxyError: Tunnel connection failed: 403 Forbidden`. `pytest -q -x infogami/infobase/tests/test_account.py` confirms an infobase setup error: `dropdb: could not translate host name "postgres" to address: Temporary failure in name resolution`. Full-suite status is therefore unknown beyond these environmental failures.
