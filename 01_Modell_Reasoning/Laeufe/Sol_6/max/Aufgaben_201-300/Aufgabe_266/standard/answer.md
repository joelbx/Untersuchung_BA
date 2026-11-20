Implemented the staged import lookup in [imports.py](/app/openlibrary/core/imports.py:20). It combines each identifier with the fixed `amazon` and `idb` sources by default, then returns matching `staged` or `pending` rows.

[ISBN resolution](/app/openlibrary/core/models.py:373) now checks both ISBN forms and loads stored import data locally when available. The existing import path remains for matching rows without stored data.

Verification: 18 focused tests passed; Ruff and `git diff --check` passed.