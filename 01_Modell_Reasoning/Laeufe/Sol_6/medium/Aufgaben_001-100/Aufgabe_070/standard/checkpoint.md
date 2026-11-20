# Checkpoint

Task: normalize non-MARC identifiers in `format_languages` and deduplicate canonical keys.

Implemented: resolve ISO 639-1 codes and English/native names with existing language helpers, validate canonical site keys, and preserve first occurrence when deduplicating. Added fixture-backed tests for the reported cases.

Verification: catalog utility tests (99 passed), add-book language tests (4 passed), Ruff checks passed, `git diff --check` passed. Black is not installed locally.
