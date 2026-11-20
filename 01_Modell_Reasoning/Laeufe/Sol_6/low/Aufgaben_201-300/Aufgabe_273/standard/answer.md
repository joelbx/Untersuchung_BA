Updated `make_work()` to return a valid `web.Storage` when either author field is missing, with an empty authors list and the required metadata defaults. It now preserves a supplied cover URL. Added the requested type annotations and regression tests.

Verification: all 13 addbook tests pass.