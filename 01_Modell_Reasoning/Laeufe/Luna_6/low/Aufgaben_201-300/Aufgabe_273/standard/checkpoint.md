# Checkpoint

Task: Fix `make_work()` handling of documents without author metadata.

Completed: Added typed module-level `make_author(key: str, name: str) -> Author`, returning the object created by `web.ctx.site.new` using an `/authors/` path. Typed `make_work(doc: dict) -> web.Storage`; missing or empty author arrays now produce an empty list, existing document fields are preserved, and `cover_url`, `ia`, and `first_publish_year` receive stable defaults when absent.

Verification: `pytest -q openlibrary/plugins/upstream/tests/test_addbook.py` — 11 passed.
