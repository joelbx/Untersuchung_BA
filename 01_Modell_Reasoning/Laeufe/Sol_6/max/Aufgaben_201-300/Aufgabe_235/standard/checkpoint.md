# Checkpoint

Task: import alternate-script author names from linked MARC 880 fields for 100, 700, and 720 author entries.

Current state: implemented `name_from_list`, retained 880 fields, and added exact subfield 6 linkage matching for personal authors from 100, 700, and 720. Updated binary expectations and added XML coverage for all three tags, multiple linked names, deduplication, and unrelated linkages.

Verification: `python -m pytest -q openlibrary/catalog/marc/tests openlibrary/catalog/merge/tests/test_merge_marc.py` finished with 132 passed and 1 existing expected failure. `git diff --check` passed.
