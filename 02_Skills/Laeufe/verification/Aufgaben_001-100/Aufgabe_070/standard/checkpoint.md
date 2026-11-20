# Checkpoint

Task: Normalize ISO-639-1 codes and English/native language names in `format_languages`, deduplicate canonical keys in first-seen order.

Implemented in `openlibrary/catalog/utils/__init__.py`: resolve existing MARC keys first, then aliases and ISO codes, then language names from the current site's records; validate resolved keys and deduplicate in input order. Added catalog tests for English and native names, ISO codes, case handling, duplicates, and invalid inputs. Existing catalog tests now set up their language site explicitly.

Verification:
- `pytest -q openlibrary/plugins/upstream/tests/test_utils.py openlibrary/tests/catalog/test_utils.py openlibrary/catalog/add_book/tests/test_load_book.py` — exit 0, 145 passed, 3 warnings.
- `ruff check openlibrary/catalog/utils/__init__.py openlibrary/tests/catalog/test_utils.py` — exit 0, all checks passed (configuration deprecation warning).
- `git diff --check` — exit 0.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local `grep`/`find`. No downloads or external research.
