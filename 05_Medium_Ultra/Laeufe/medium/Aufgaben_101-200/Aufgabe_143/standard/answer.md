Centralized `add_db_name` in [catalog utils](/app/openlibrary/catalog/utils/__init__.py). Every expanded edition now receives generated author identifiers, and existing editions pass author names and birth/death dates through the same expansion path. The comparator also recognizes equivalent names in reversed comma order.

Verification: 71 relevant tests passed; Ruff and `git diff --check` passed.