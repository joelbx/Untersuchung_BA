Issue: author matching with varied date formats, honorifics, and literal asterisks.
Status: implemented and verified.
Changes: string-based honorific removal with normalized exceptions; four-digit year extraction; staged exact/alternate/surname matching with year checks; escaped asterisk searches plus exact-value fallback for literal asterisks; original fields retained for unmatched authors; regression tests added.
Verification: pytest -q openlibrary/catalog/add_book/tests -> 160 passed, 1 xfailed. Ruff check and git diff --check passed.
