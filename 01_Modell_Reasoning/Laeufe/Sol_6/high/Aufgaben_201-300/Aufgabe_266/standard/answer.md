Added `STAGED_SOURCES` and `ImportItem.find_staged_or_pending` in [imports.py](/app/openlibrary/core/imports.py). The method returns matching staged or pending rows for every source and identifier combination. ISBN resolution now uses it with both ISBN-13 and ISBN-10 in [models.py](/app/openlibrary/core/models.py).

Verification: 17 relevant tests passed; Ruff and `git diff --check` passed.