Task: Expand MARC contributor role mapping and preserve author roles in new works.
Status: implemented and verified.
Changes: ROLES mapping; $e/$4 parsing with $4 precedence; ordered work author roles; author count check; focused tests and updated MARC expectations.
Verification: 162 tests passed in MARC parser and add-book suites; ruff check passed.
