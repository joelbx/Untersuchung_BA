# Checkpoint

- Task: extract role entry point documentation building into `RoleMixin._build_doc`.
- Starting state: working tree has no reported changes; implementation is in `lib/ansible/cli/doc.py`.
- Implemented `RoleMixin._build_doc` and changed `_create_role_doc` to consume its `(fqcn, doc)` result.
- Verified: `PYTHONPATH=lib pytest -q test/units/cli/test_doc.py` (14 passed); direct `_build_doc` assertions for naming, filtering, full specs, and empty results; existing role documentation CLI fixture checks for normal and collection roles passed.
