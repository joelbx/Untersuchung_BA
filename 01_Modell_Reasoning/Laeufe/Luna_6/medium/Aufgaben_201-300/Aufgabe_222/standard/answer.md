Extracted role documentation construction into `RoleMixin._build_doc`. It returns `(fqcn, doc)` with the existing `path`, `collection`, and `entry_points` keys, or `(fqcn, None)` when there are no matching entry points. `_create_role_doc` now uses the returned tuple.

Verification: `python -m pytest test/units/cli/test_doc.py` passed (14 tests), and `git diff --check` passed.