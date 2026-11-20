Updated `make_work()` to handle missing author fields, preserve provided metadata, and apply the requested defaults. `make_author()` now has the specified annotations and creates authors through `web.ctx.site.new`.

Verification: `python -m pytest openlibrary/plugins/upstream/tests/test_addbook.py -q` — 11 passed.