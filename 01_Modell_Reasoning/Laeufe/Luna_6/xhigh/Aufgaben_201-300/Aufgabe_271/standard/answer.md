Implemented the ImportAPI publisher parsing and ISBN classification changes.

- IA publisher values now produce a `publishers` list, and location-bearing values are split into ordered `publish_places` and `publishers`.
- Added `get_colon_only_loc_pub` and `get_location_and_publisher`; retained the legacy publisher helper for compatibility.
- Moved `get_isbn_10_and_13` to [isbn.py](/app/openlibrary/utils/isbn.py:88), and ImportAPI now imports it there.

Verification: 35 relevant existing tests passed; `git diff --check` passed. Updated `.codex-role-output/checkpoint.md`.