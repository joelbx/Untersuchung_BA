# Checkpoint

Task: Normalize non-MARC identifiers in `format_languages` and deduplicate canonical keys in first-occurrence order.
Status: Implemented and verified. Language records provide ISO-639-1 and translated/native name lookup; existing MARC mapping is used as fallback. Invalid and ambiguous values raise `InvalidLanguage`.
Tests: `pytest -q openlibrary/tests/catalog/test_utils.py --reruns 0` (101 passed); `ruff check` (passed); `git diff --check` (passed).
Delegation: none; solved directly.
