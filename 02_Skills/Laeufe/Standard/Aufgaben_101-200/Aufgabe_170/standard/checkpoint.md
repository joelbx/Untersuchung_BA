# Checkpoint

Issue: make edition matching expand raw records consistently, including author names, titles, ISBNs, and metadata.

Completed: moved `add_db_name` and `expand_record` into `merge_marc`, with `catalog.utils` importing the shared functions. Added `threshold_match`; `editions_match` expands raw inputs through it. Author and contributor names, title variants, ISBN variants, and valid publish countries are included in expansion. Updated the add-book matching import and added regression cases for raw records without ISBNs and contributor enrichment.

Verification: `pytest -q openlibrary/catalog/merge/tests/test_merge_marc.py openlibrary/tests/catalog/test_utils.py openlibrary/catalog/add_book/tests/test_match.py` passed (67 passed, 2 existing xfailed). `git diff --check` passed.

Tooling note: `rg` was unavailable (`/bin/bash: line 1: rg: command not found`); used `grep` and `find` for inspection. This did not block verification.
