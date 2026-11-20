Extracted `RoleMixin._build_doc` in [doc.py](/app/lib/ansible/cli/doc.py). It returns `(fqcn, doc)` with the original entry point specifications, or `(fqcn, None)` when none are included. `_create_role_doc` now adds only returned docs.

Added focused coverage in [test_doc.py](/app/test/units/cli/test_doc.py). All 21 tests pass with `PYTHONPATH=lib`; `git diff --check` passes.