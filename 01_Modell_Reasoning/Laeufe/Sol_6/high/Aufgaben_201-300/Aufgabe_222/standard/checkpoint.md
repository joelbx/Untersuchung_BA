# Checkpoint

Task: Extract RoleMixin role entry-point documentation logic into `_build_doc`.

Status: Complete.

Changes:
- Added `RoleMixin._build_doc(role, path, collection, argspec, entry_point=None)` returning `(fqcn, doc)` or `(fqcn, None)` when no entry points match.
- Updated `_create_role_doc` to add only returned documentation objects.
- Added direct and caller-level unit coverage for naming, data preservation, filtering, and empty results.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/cli/test_doc.py` passed (20 tests). `git diff --check` passed.
