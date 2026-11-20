# Best Book Awards checkpoint

Implemented nomination persistence in `openlibrary/core/bestbook.py` and table DDL in `openlibrary/core/schema.sql`, with read-status and uniqueness validation, list/count/leaderboard, update and removal. Added work accessors, awards and count JSON endpoints, work redirect updates and counts, and account anonymization updates and reporting.

Verification:
- `ruff check openlibrary/core/bestbook.py openlibrary/core/bookshelves.py openlibrary/core/models.py openlibrary/plugins/openlibrary/api.py openlibrary/accounts/model.py openlibrary/plugins/admin/code.py openlibrary/tests/core/test_bestbook.py` — passed.
- `python -m pytest openlibrary/tests/core/test_models.py openlibrary/tests/accounts/test_models.py openlibrary/tests/core/test_bestbook.py openlibrary/tests/core/test_db.py -q` — 49 passed.
- `git diff --check` — passed.

The repository's SQL bootstrap applies `openlibrary/core/schema.sql` to new databases. For existing databases, `scripts/migrate-bestbook.sql` provides idempotent DDL for the normal database deployment process; this checkout does not provide a migration runner for this application schema.
