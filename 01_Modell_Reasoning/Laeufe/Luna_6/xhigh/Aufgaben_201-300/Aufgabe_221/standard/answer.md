Implemented Best Book Awards persistence and APIs.

- Added [bestbook.py](/app/openlibrary/core/bestbook.py) with add, update, remove, listing, count, and leaderboard methods. Read status and uniqueness are enforced, with database constraints as a concurrency guard.
- Added the awards POST and count GET endpoints in [api.py](/app/openlibrary/plugins/openlibrary/api.py), including JSON authentication and validation errors.
- Added the `Already Read` check, Work award accessors, redirect count/reference handling, and anonymization updates in [bookshelves.py](/app/openlibrary/core/bookshelves.py), [models.py](/app/openlibrary/core/models.py), and [model.py](/app/openlibrary/accounts/model.py). Added the table and uniqueness constraints to [schema.sql](/app/openlibrary/core/schema.sql).

Verification passed: Ruff, Python compile checks, `git diff --check`, and 46 existing DB, model, and account tests. The repository has no dedicated Bestbook tests.