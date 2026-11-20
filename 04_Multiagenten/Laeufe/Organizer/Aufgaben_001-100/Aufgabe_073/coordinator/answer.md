Amazon imports now include unique, human-readable language values from edition metadata, excluding entries marked “Original Language.” The `languages` key is omitted when no values remain, and the metadata cleaner preserves it for import.

The vendor test suite passed (36 tests). Ruff lint and `git diff --check` passed. No delegation was used.