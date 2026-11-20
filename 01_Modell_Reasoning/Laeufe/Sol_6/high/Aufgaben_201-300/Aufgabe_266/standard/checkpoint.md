# Checkpoint

Task: improve ISBN resolution using locally staged or pending import items.

Implemented:
- Added fixed `STAGED_SOURCES` tuple and `ImportItem.find_staged_or_pending` in `openlibrary/core/imports.py`.
- Reused that lookup from `Edition.from_isbn` with both ISBN-13 and ISBN-10 variants; catalog lookup now checks both variants.
- Added database and ISBN resolution tests.

Verification: relevant core tests and Ruff lint passed. No external research or downloads were used.
