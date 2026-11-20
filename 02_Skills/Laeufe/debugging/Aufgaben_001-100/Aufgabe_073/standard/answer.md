Amazon imports now include unique language names from edition metadata, preserving Amazon’s casing and order. Entries marked `Original Language` are excluded, and `languages` is omitted when no values remain. The load cleaner now preserves the field.

The vendor test suite passes (36 tests), as do Ruff lint and `git diff --check`.