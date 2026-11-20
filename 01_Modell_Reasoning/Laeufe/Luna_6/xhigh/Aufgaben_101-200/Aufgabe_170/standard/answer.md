Implemented edition expansion and matching in [merge_marc.py](/app/openlibrary/catalog/merge/merge_marc.py:54). Raw and pre-expanded records now use the same scoring path; missing metadata and author/contributor comparisons are handled safely.

Verification passed: merge tests (7 passed, 1 xfailed), add-book matching tests (1 passed, 1 xfailed), Ruff, and direct checks of the new API.