Edition matching now accepts raw import records. [merge_marc.py](/app/openlibrary/catalog/merge/merge_marc.py:54) adds author enrichment, record expansion, and threshold matching; the add book path uses the new matcher. Matching also handles missing titles, ISBNs, and authors without errors.

Verification: 156 tests passed, 1 skipped, and 2 expected failures. Ruff and `git diff --check` passed.