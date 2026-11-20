# Checkpoint

Task: Extract role entry-point documentation construction from `RoleMixin` into `_build_doc` in `ansible.cli.doc`.

Completed: Added `_build_doc(role, path, collection, argspec, entry_point=None)`, returning `(fqcn, doc)` or `(fqcn, None)` when no entry points are included. Updated `_create_role_doc` to consume the tuple and preserve the existing documentation keys and values.

Verification: `python -m pytest -q test/units/cli/test_doc.py` passed (14 tests). `git diff --check` passed. No existing unit tests directly cover `_create_role_doc`.
