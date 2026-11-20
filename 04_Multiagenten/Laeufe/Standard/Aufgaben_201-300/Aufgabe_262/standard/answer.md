Book imports now remove the `cover` field and upload its URL only when it uses HTTP or HTTPS and its hostname matches `ALLOWED_COVER_HOSTS`, ignoring case. The reusable `process_cover_url` helper is used for both new and matched editions.

All 89 add_book tests passed, and Ruff checks passed.