Extracted the role entry point logic into `RoleMixin._build_doc`. It returns `(fqcn, doc)` or `(fqcn, None)` when no entry points match, and `_create_role_doc` now uses that result. Added tests for the returned fields, filtering, and caller behavior.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/cli/test_doc.py` passed (20 tests), and `git diff --check` passed.