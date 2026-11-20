Implemented record expansion and matching in [merge_marc.py](/app/openlibrary/catalog/merge/merge_marc.py).

`editions_match` now expands both records before scoring. Added `add_db_name`, `expand_record`, and `threshold_match`; expansion handles missing authors, contributor names, title variants, ISBN variants, and invalid publication countries.

Verification passed: merge tests (7 passed, 1 expected failure), add-book matching tests (1 passed, 1 expected failure), Ruff, and manual edge checks.