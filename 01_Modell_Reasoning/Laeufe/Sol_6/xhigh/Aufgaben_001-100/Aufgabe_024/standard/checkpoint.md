# Author matching fix

Status: complete.

Implemented string-based honorific removal with exception handling, strict four-digit year extraction, year-aware exact/alternate/surname matching, literal asterisk handling, and full-field preservation for new authors. Added regression coverage for mixed date formats, fallback priority, honorific edge cases, wildcard names, and query year patterns.

Verified: `python -m pytest -q openlibrary/catalog/add_book/tests openlibrary/tests/core/test_helpers.py openlibrary/tests/catalog/test_utils.py` (264 passed, 1 expected failure); `ruff check` passed for edited Python files; `git diff --check` passed.
