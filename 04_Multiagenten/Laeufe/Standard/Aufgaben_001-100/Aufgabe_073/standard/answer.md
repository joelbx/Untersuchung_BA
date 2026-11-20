Amazon imports now include language names from edition metadata when available. Serialization excludes entries marked `Original Language`, removes duplicates, preserves Amazon’s casing, and omits `languages` when the result is empty. The load cleanup also preserves the field.

Verification: all 37 vendor tests pass, and Ruff and `git diff --check` pass.