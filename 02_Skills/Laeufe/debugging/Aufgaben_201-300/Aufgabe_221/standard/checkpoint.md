# Best Book Awards checkpoint

Investigation started. `rg` is unavailable in this environment, so repository searches use `find` and `grep`. No code changes yet.

Root cause: the server has no awards table, model, or route. Comparable ratings and bookshelves persist in `core/schema.sql` via `CommonExtras`; work redirects and account anonymization explicitly enumerate each auxiliary table. Consequently all four workflows omit awards. The read state is available through `Bookshelves.get_users_read_status_of_work`, which returns shelf id 3 for Already Read.

Hypothesis: adding a constrained awards table and a `CommonExtras` model, then wiring it into those explicit enumeration points, will provide durable nominations and keep redirects/anonymization consistent. A focused failing test will establish the missing interface first.

Implemented `bestbook` persistence with database uniqueness constraints, read prerequisite, list/count/leaderboard/add/update/remove methods, Work accessors, JSON APIs, and redirect/anonymization integration. The API accepts form and JSON bodies. `core/schema.sql` is the repository's database initialization schema; existing deployments must apply the new table DDL before using these endpoints.

Verification: the initial `python -m pytest -q openlibrary/tests/core/test_bestbook.py` failed as expected with `ModuleNotFoundError: No module named 'openlibrary.core.bestbook'`. After implementation, `python -m pytest -q openlibrary/tests/core/test_bestbook.py openlibrary/tests/core/test_db.py openlibrary/tests/core/test_models.py openlibrary/tests/accounts` passed (49 tests). `python -m ruff check` on changed Python files and `git diff --check` passed. No external research or downloads were used.
