Extracted role entry-point documentation into `RoleMixin._build_doc` in [doc.py](/app/lib/ansible/cli/doc.py). It returns `(fqcn, doc)` or `(fqcn, None)` when no entry points match; `_create_role_doc` now uses that result.

Added coverage in [test_doc.py](/app/test/units/cli/test_doc.py). All 20 unit tests pass, and the existing local-role and filtered collection-role output fixtures match.