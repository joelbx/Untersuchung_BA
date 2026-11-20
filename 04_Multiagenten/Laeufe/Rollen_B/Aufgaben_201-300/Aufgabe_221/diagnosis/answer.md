The issue spans the award model, API, and two existing workflows:

- [core/schema.sql](/app/openlibrary/core/schema.sql) has no nominations table. A new table needs constraints for both `(username, work_id)` and `(username, topic)` so concurrent requests cannot create duplicates.
- [bookshelves.py](/app/openlibrary/core/bookshelves.py:631) exposes read status, but lacks `user_has_read_work`. “Already Read” is shelf `3`.
- [api.py](/app/openlibrary/plugins/openlibrary/api.py:128) has comparable work endpoints, but no award or award-count endpoint. Award requests need the specified JSON responses, including authentication and validation errors.
- [models.py](/app/openlibrary/core/models.py:463) lacks the three `Work` award methods. Its [redirect workflow](/app/openlibrary/core/models.py:644) counts and updates other patron data but omits awards.
- [account model](/app/openlibrary/accounts/model.py:334) and [admin summary](/app/openlibrary/plugins/admin/code.py:454) omit nominations during anonymization.

One implementation choice needs care: a work redirect can collide with an existing nomination for the destination work, so the redirect update must preserve the uniqueness rules and report its outcome accurately. I found no existing award tests. I recorded the findings in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md); project source and tests remain unchanged under this run’s fault-localization scope.