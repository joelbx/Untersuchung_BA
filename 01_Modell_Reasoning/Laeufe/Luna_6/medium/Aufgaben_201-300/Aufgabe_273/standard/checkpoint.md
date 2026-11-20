# Checkpoint

Task: resolve `make_work()` failure on documents without author fields.

Implemented in `openlibrary/plugins/upstream/addbook.py`:
- Added the requested `dict -> web.Storage` annotation.
- Added the requested `str` argument and `Author` return annotations to the nested author builder. It prefixes `/authors/`, calls `web.ctx.site.new` with the path and author data, and returns that created object.
- Author creation now safely zips optional key/name lists; missing or unmatched information results in an empty/partial author list without raising `KeyError`.
- Preserves supplied cover metadata and defaults missing `cover_url`, `ia`, and `first_publish_year` values.

Verification: `python -m pytest openlibrary/plugins/upstream/tests/test_addbook.py -q` — 11 passed.
