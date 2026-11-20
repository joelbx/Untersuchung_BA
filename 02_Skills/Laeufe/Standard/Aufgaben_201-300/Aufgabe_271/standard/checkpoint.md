# Checkpoint

Implemented compound publisher parsing in upstream utils and wired the IA fallback to it. Moved raw ISBN classification to `openlibrary/utils/isbn.py` and added regression tests.

Checks:
- `python -m pytest -q -o reruns=0 openlibrary/plugins/upstream/tests/test_utils.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/utils/tests/test_isbn.py` — 51 passed, 2 dependency warnings.
- `git diff --check` — passed.
- `python -m ruff check openlibrary/plugins/importapi/code.py openlibrary/plugins/upstream/utils.py openlibrary/utils/isbn.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/upstream/tests/test_utils.py` — could not run: `/usr/local/bin/python: No module named ruff`. Ruff-specific lint results remain unverified; no dependencies were downloaded.
