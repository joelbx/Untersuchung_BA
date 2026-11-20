# Checkpoint

Task: Resolve edition matching and record expansion in `openlibrary/catalog/merge/merge_marc.py`.

Status: Complete.

Changes: Moved record expansion and author name enrichment into merge_marc, retained utility imports, expanded both records during threshold comparison, handled missing author data, enriched contributors, and included page count in add_book's existing-edition comparison. Added raw-record and threshold tests and enabled the previously expected-failure integration match.

Verification: 132 passed, 1 pre-existing expected failure in the focused merge, catalog utility, and add_book suites. Ruff check and git diff --check passed.
