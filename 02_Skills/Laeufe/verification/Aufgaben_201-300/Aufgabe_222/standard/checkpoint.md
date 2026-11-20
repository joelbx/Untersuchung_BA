# Checkpoint

Task: Extract `RoleMixin._build_doc` for role entry point documentation, preserving existing output and filtering behavior.

Status: Implementation and verification complete.

Changes:
- Added `RoleMixin._build_doc` returning `(fqcn, doc)` or `(fqcn, None)` when no entry points match.
- Updated `_create_role_doc` to consume the tuple and omit missing documentation.
- Added direct unit coverage for names, fields, full specifications, filtering, empty matches, and caller integration.

Verification:
- `python -m pytest -q test/units/cli/test_doc.py` failed (4 tests) because it imported `/usr/local/lib/python3.9/dist-packages/ansible/cli/doc.py` rather than the repository package; the error was `AttributeError: 'RoleMixin' object has no attribute '_build_doc'`.
- `PYTHONPATH=lib python -m pytest -q test/units/cli/test_doc.py` passed: 20 passed in 0.19s.
- `git diff --check` passed (exit 0).
