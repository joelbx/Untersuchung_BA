Amazon imports now include human-readable edition languages when present. The serializer excludes entries marked `Original Language`, removes duplicates while preserving order and casing, and omits the field when no languages remain. The metadata cleaner now preserves `languages`.

Verification: 36 vendor tests passed; Ruff and `git diff --check` passed.