Task: Resolve inconsistent edition matching and record expansion in openlibrary/catalog/merge/merge_marc.py.
Status: Complete. Added add_db_name, expand_record, and threshold_match in merge_marc. editions_match now expands raw inputs; catalog.utils re-exports the helpers for existing callers. Added regression tests for raw records, ISBN aggregation, author/contributor names, and thresholds 875/515.
Verification: 13 passed, 2 existing xfailed in merge_marc and add_book match tests. Ruff check and git diff --check passed.
