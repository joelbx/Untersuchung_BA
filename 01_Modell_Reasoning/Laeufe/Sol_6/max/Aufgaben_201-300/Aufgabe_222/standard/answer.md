Extracted role entry point documentation building into `RoleMixin._build_doc` in [doc.py](/app/lib/ansible/cli/doc.py:232). It returns `(fqcn, doc)` and returns `(fqcn, None)` when no entry points match. `_create_role_doc` now uses that result without shared state.

Verification passed: 14 unit tests, direct checks of the new method, and the existing role CLI fixture checks.