Implemented Best Book Awards persistence, validation, work accessors, API endpoints, redirect updates, and anonymization support.

Verification passed: `compileall`, `git diff --check`, and the existing core database/model tests (42 passed).

The new table is in [schema.sql](/app/openlibrary/core/schema.sql), and the implementation is in [bestbook.py](/app/openlibrary/core/bestbook.py).