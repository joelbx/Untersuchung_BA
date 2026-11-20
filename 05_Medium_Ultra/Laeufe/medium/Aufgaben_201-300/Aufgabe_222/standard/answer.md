Extracted the role entry point logic into `RoleMixin._build_doc`. It returns `(fqcn, doc)` and returns `(fqcn, None)` when no entry points match; `_create_role_doc` now uses that result.

Added unit coverage for filtering, full specification objects, naming, and omitted results. The relevant test file passes: **20 tests** with `PYTHONPATH=lib`.