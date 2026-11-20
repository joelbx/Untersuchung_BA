# Checkpoint

Implemented language-aware Wikipedia sitelinks, valid Wikidata statement extraction, structured Wikipedia/Wikidata/Google Scholar profiles, author infobox rendering, and local SVG icons. Restored `Author.wikidata()` lookup, which had an unconditional early return.

TDD: new tests failed first on the missing `_get_wikipedia_link` method and missing infobox links. They pass after the implementation.

Checks:
- `pytest -q openlibrary/tests/core/test_wikidata.py openlibrary/tests/core/test_models.py --reruns 0`: 43 passed (before infobox test was added).
- `pytest -q openlibrary/tests/core/test_models.py::TestAuthor::test_infobox_displays_wikidata_external_profiles --reruns 0`: 1 passed.
- `ruff check openlibrary/core/wikidata.py openlibrary/core/models.py openlibrary/tests/core/test_wikidata.py openlibrary/tests/core/test_models.py`: passed, with existing project config deprecation warning.
- `pytest -q --reruns 0`: failed; 2229 passed, 21 skipped, 9 xfailed, 78 errors. Collection included `scripts/tests/test_isbndb.py`, which imports a module that requests `https://raw.githubusercontent.com/internetarchive/openlibrary-client/master/olclient/schemata/import.schema.json`; proxy returned `403 Forbidden` (`requests.exceptions.ProxyError`). Several `infogami/infobase` and `vendor/infogami/test/test_dbstore.py` tests errored because required database services are unavailable. This full suite is not green in the current environment.
- `pytest -q --reruns 0 --maxfail=1`: confirmed the same blocked schema request.
- `pytest -q openlibrary/tests/core --reruns 0`: 161 passed, 2 xfailed, 1 failed: `openlibrary/tests/core/test_lending.py::TestGetAvailability::test_cache` fails because `web.ctx.env` is absent. This appears unrelated to the Wikidata change.
- `ruff check ...; black --check ...`: Ruff passed, but `black` is unavailable (`/bin/bash: line 1: black: command not found`). Formatting with Black remains unverified. `ruff format --check ...` reports reformatting of all four files, including unrelated pre-existing formatting; its style differs from project Black configuration, so it was not applied.
- Final focused run: `pytest -q openlibrary/tests/core/test_wikidata.py openlibrary/tests/core/test_models.py --reruns 0`: 44 passed, with 3 pre-existing dependency deprecation warnings.
- Final `ruff check` and `git diff --check`: passed.
