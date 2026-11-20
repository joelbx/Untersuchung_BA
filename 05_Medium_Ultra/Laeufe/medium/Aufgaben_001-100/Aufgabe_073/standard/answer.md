Amazon imports now include language names from edition metadata when available. The serializer excludes entries marked “Original Language,” removes duplicates while preserving the supplied names and order, and omits `languages` when the list is empty. The load cleaner now preserves the field.

Verification: all 37 vendor tests passed; Ruff and `git diff --check` passed.