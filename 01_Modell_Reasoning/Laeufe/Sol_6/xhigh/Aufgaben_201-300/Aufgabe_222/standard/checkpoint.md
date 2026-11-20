# Checkpoint

Task: Extract role entry-point documentation construction into `RoleMixin._build_doc` while preserving current consumers.

Status: Complete.

Changes:
- Added `RoleMixin._build_doc` returning `(fqcn, doc)` or `(fqcn, None)` for no matching entry points.
- Updated `_create_role_doc` to consume returned documentation.
- Preserved full input specification values and made text rendering tolerate a null specification.
- Added unit coverage for qualification, filtering, omissions, preserved specifications, and caller behavior.

Verification:
- `PYTHONPATH=lib pytest -q test/units/cli/test_doc.py`: 20 passed.
- Existing local-role and filtered collection-role integration output fixtures: both matched.
- `git diff --check`: passed.
