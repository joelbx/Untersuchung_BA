# Checkpoint

Implemented `add_db_name`, `expand_record`, and `threshold_match` in `openlibrary/catalog/merge/merge_marc.py`; `editions_match` now expands raw records through `threshold_match`. `catalog.utils` re-exports the shared helpers. Added regression coverage for raw records, incomplete author dates, contributors, missing ISBNs and titles, and thresholds 875/515. Merge and add-book matching tests passed (with two existing expected failures); the larger add-book test file passed. Ruff and `git diff --check` passed. Final focused test run follows the last threshold assertion edit.
