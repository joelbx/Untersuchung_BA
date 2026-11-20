Extracted `RoleMixin._build_doc` and updated `_create_role_doc` to use its `(fqcn, doc)` result. The method preserves the path, collection, and full entry point specifications, and returns `(fqcn, None)` when no entry points match.

Added focused tests. The local doc test module passes: **18 passed** with `PYTHONPATH=./lib`.