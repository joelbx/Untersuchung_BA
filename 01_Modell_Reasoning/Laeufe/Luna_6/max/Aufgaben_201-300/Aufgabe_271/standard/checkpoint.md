# Checkpoint

Task: fix ImportAPI publisher/location parsing and ISBN classification per the issue.

Implemented:
- Added `get_colon_only_loc_pub` and defensive `get_location_and_publisher` parsing in upstream utilities, including semicolon locations/pairs, unidentified-place cleanup, comma fallback, bracket removal, and malformed extra-colon handling.
- Updated IA record construction to always include a publishers list and parse each publisher string through the new helper.
- Added length-only, whitespace-trimming `get_isbn_10_and_13` to `openlibrary.utils.isbn`; ImportAPI imports it there. The upstream module retains a compatibility re-export for its existing callers/tests.

Verification: focused existing tests passed (35 total), and direct smoke checks passed for the reported metadata, parser edge cases, and ISBN classification. `git diff --check` is clean.
