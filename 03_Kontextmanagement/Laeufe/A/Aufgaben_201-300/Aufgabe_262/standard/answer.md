Book imports now upload covers only when the URL uses HTTP or HTTPS and its host matches `ALLOWED_COVER_HOSTS`, ignoring case. The new [`process_cover_url`](/app/openlibrary/catalog/add_book/__init__.py:100) helper removes the `cover` key and is used for both new and matched editions.

Verification: 150 `add_book` tests passed, 1 was expected to fail, and lint passed.