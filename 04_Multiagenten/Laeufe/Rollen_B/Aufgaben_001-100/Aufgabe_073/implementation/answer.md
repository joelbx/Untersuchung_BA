Amazon serialization now reads language display values from edition metadata, excludes entries marked “Original Language,” removes duplicates, and includes `languages` only when values remain. The metadata cleaner preserves the field.

All 36 vendor tests pass, including the new language cases. `ruff check` and `git diff --check` pass.