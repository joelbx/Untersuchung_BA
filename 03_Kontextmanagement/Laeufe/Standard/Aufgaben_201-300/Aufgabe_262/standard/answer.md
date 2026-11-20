Book imports now skip cover uploads when the URL’s host is outside `ALLOWED_COVER_HOSTS`. The new `process_cover_url` helper removes the `cover` key and accepts allowed hosts case-insensitively over HTTP or HTTPS. Both new and matched edition imports use it.

Verification: 88 add-book tests passed; Ruff and `git diff --check` passed.