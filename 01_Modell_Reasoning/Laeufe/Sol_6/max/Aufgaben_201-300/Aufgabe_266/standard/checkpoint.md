# ISBN staged import lookup

- Added `STAGED_SOURCES` and `ImportItem.find_staged_or_pending` with source/identifier combinations and staged/pending filtering.
- Updated `Edition.from_isbn` to check ISBN 13 and ISBN 10, load staged JSON through the local book loader, and keep the prior fallback for rows without data.
- Added database lookup and ISBN resolution tests. The focused core test run passed: 18 tests; the import tests passed again after the final SQL edit (7 tests).
- Ruff and `git diff --check` passed. Final review complete.
