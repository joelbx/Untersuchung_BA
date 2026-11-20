Added `STAGED_SOURCES` and `ImportItem.find_staged_or_pending` in [imports.py](/app/openlibrary/core/imports.py). The ISBN lookup in [models.py](/app/openlibrary/core/models.py) now uses local staged or pending records for ISBN-13 and ISBN-10 matches.

Verification: 16 relevant tests passed; Ruff and `git diff --check` passed.