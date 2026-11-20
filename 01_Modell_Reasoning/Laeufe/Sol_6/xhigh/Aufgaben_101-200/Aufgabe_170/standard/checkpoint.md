# Checkpoint

Task: resolve inconsistent edition matching and record expansion in `openlibrary/catalog/merge/merge_marc.py`.

Status: implemented. `merge_marc` now owns `add_db_name`, `expand_record`, and `threshold_match`; `catalog.utils` re-exports the helpers. Both merge and add-book matching accept raw records, including records with missing ISBNs or titles. Author/contributor matching supports catalog name order, and the existing edition's page count is included.

Verification: `pytest -q openlibrary/catalog/merge/tests openlibrary/catalog/add_book/tests --disable-warnings --reruns 0` passed (113 passed, 1 skipped, 1 pre-existing xfailed). `ruff check` on changed Python files and `git diff --check` passed.

Constraints: use repository code and existing tests only; preserve git history, index baseline, and harness configuration.
