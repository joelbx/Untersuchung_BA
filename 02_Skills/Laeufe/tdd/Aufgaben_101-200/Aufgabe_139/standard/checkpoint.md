# Checkpoint

Implemented test-first augmentation of incomplete promise records using ISBN-10 first, then B* ASIN; staged metadata fills empty fields before builder validation. Validation now accepts complete records or records with title, source records, and a strong identifier. The batch staging path handles lookup failures and emits total/incomplete gauges. Placeholder publishers are cleared before augmentation.

Verification:
- Focused import, catalog, script, and stats tests passed; the restored `format_date` test also passed.
- Full command `pytest -q . --ignore=infogami --ignore=vendor --ignore=node_modules` failed during collection of `scripts/tests/test_isbndb.py` and `scripts/tests/test_partner_batch_imports.py`: both import paths call `requests.get` for `https://raw.githubusercontent.com/internetarchive/openlibrary-client/master/olclient/schemata/import.schema.json` and raise `requests.exceptions.ProxyError` (`Tunnel connection failed: 403 Forbidden`). The remaining executed tests reported 1903 passed, 9 skipped, 16 xfailed, 54 xpassed.
- Final full suite excluding those two network-dependent modules: 1907 passed, 9 skipped, 16 xfailed, 54 xpassed.
- `ruff check` and `git diff --check` passed (with an existing Ruff config deprecation warning).

Remaining uncertainty: the two network-dependent test modules cannot be collected offline. No downloads attempted.
