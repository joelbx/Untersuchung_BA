# Checkpoint

Implemented `RoleMixin._build_doc` in `lib/ansible/cli/doc.py`. It computes the role FQCN and returns a standalone documentation mapping with `path`, `collection`, and matching full entry point specs, or `None` when no entry points remain. `_create_role_doc` now inserts only returned documents, keeping the prior consumer shape.

Verification: `python -m pytest test/units/cli/test_doc.py` passed (14 tests); `git diff --check` passed.
