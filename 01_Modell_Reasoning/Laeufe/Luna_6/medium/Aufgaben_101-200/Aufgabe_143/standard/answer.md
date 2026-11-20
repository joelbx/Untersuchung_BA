Implemented centralized author identifier generation in [catalog/utils/__init__.py](/app/openlibrary/catalog/utils/__init__.py). `expand_record` now ensures every author gets a `db_name`, including a name-only identifier when no dates are available. Existing-edition conversion now supplies author name and birth/death dates, leaving identifier generation to expansion.

Removed the duplicate implementations while keeping `add_book.add_db_name` available through its import.

Verification: relevant tests passed: 64 passed, 1 xfailed, 1 xpassed. `git diff --check` passed.