# Checkpoint

Task: Extract RoleMixin role entry point documentation construction into `_build_doc`.

Completed: `_build_doc` returns `(fqcn, doc)` or `(fqcn, None)` and preserves path, collection, and full entry point specs. `_create_role_doc` consumes that tuple and omits unmatched roles. Added direct and caller coverage.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/cli/test_doc.py` (20 passed); `git diff --check` passed.

Delegation: none.
