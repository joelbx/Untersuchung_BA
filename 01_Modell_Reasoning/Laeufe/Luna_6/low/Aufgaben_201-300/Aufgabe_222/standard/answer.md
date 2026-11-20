Extracted role documentation construction into `RoleMixin._build_doc`, which returns `(fqcn, doc)` and returns `(fqcn, None)` when no entry points match. `_create_role_doc` now uses that result while preserving the `path`, `collection`, and `entry_points` keys.

Validation: `test/units/cli/test_doc.py` passed (14 tests), and `git diff --check` reported no issues.