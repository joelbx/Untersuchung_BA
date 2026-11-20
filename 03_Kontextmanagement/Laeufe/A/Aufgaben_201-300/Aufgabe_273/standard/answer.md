Fixed `make_work()` so documents missing either or both author fields return a `web.Storage` work with an empty `authors` list. It preserves supplied fields and applies the requested metadata defaults. I also added the requested `make_author()` and `make_work()` type annotations.

The relevant tests pass: **15 passed**.