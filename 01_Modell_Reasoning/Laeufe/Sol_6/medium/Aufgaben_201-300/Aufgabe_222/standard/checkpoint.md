# Checkpoint

Task: Extract RoleMixin entry point documentation builder into `_build_doc`.

Status: Complete. `_create_role_doc` delegates to `_build_doc`; the builder returns `(fqcn, doc)` or `(fqcn, None)` for empty or filtered-out entry points. Added focused unit tests for naming, filtering, unchanged metadata, full specifications, and empty input.

Verification: `PYTHONPATH=./lib python -m pytest -q test/units/cli/test_doc.py` — 18 passed.
