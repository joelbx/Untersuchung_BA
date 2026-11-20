Extracted `RoleMixin._build_doc` in [doc.py](/app/lib/ansible/cli/doc.py). It returns `(fqcn, doc)`, or `(fqcn, None)` when no entry point matches, while preserving the path, collection, and full entry point specifications. Added focused tests in [test_doc.py](/app/test/units/cli/test_doc.py).

Verification: **19 tests passed**; `git diff --check` passed.