# Checkpoint

Task: Resolve inconsistent edition matching and record expansion in `openlibrary/catalog/merge/merge_marc.py`.

Initial findings: `editions_match` is implemented there; existing coverage is in `openlibrary/catalog/merge/tests/test_merge_marc.py`. `rg` is unavailable in this environment, so searches use standard utilities.

Next: inspect implementation and tests, make focused changes, run relevant existing tests.
