Book imports now remove the `cover` field and send its URL to the cover store only when `process_cover_url` accepts its HTTP or HTTPS host. The check covers both new and matched editions in [add_book/__init__.py](/app/openlibrary/catalog/add_book/__init__.py:354).

I delegated the host investigation and regression tests, then reviewed the combined patch. The proxy’s authoritative allow-list is not in this checkout, so `ALLOWED_COVER_HOSTS` uses hosts evidenced by local import code and tests.

Validation: **150 passed, 1 expected failure** in the `add_book` test package; Ruff and `git diff --check` passed.