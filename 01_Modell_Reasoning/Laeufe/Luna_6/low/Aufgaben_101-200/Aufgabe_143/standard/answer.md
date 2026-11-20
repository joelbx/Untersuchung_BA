Centralized `db_name` generation in [catalog/utils/__init__.py](/app/openlibrary/catalog/utils/__init__.py). `expand_record` now adds identifiers to author dictionaries, and edition matching rebuilds comparable authors from their name and available date fields before expansion. Removed the duplicate generators.

Added tests for date formatting, missing or empty authors, and automatic generation during expansion.

Verification: **121 passed, 1 xfailed, 1 xpassed** across the focused catalog tests.