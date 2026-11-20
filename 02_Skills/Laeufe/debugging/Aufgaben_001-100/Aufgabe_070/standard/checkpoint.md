# Checkpoint

Task: normalize ISO-639-1 codes and English/native language names in `format_languages`, then deduplicate canonical keys in first-seen order.

Status: investigating root cause and existing tests. No fix attempted yet.

Investigation: `format_languages` only lowercases the token and checks `/languages/{token}`. It has no conversion or seen-key tracking. `get_marc21_language` contains ISO-639-1 and English-name mappings; `get_abbrev_from_full_lang_name` resolves site language names and translated native names. Existing focused tests fail at `web.ctx.site` because they omit `mock_site` fixture (command: `python -m pytest openlibrary/tests/catalog/test_utils.py -q -k format_language`, exit 1, AttributeError). Existing test fixture `add_languages` populates language records for integration tests. Hypothesis: resolve alternate identifiers using existing lookup helpers, validate canonical site key, then append only unseen keys.

Implementation: `format_languages` preserves valid MARC keys, resolves other tokens using the existing MARC alias table and full-name helper, validates the resolved site key, and deduplicates canonical keys in input order. Ambiguous or missing names still raise `InvalidLanguage`. Tests now use an explicit mock language site and cover English/native names, ISO codes, deduplication, missing mapped codes, and ambiguous names.

Verification: `python -m pytest openlibrary/tests/catalog/test_utils.py openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/plugins/upstream/tests/test_utils.py -q --reruns 0` passed (151 tests). `python -m ruff check openlibrary/catalog/utils/__init__.py openlibrary/tests/catalog/test_utils.py && git diff --check` passed. Warnings are existing pytest/ruff configuration and dependency deprecations.
