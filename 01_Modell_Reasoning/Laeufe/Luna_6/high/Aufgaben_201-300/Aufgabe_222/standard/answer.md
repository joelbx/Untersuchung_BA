Extracted the logic into `RoleMixin._build_doc` in [doc.py](/app/lib/ansible/cli/doc.py). It returns the role FQCN and a documentation dict with the existing keys, or `(fqcn, None)` when no entry points match. `_create_role_doc` now uses that result.

Verification: `test/units/cli/test_doc.py` passed (14 tests), and `git diff --check` passed.