# Checkpoint

Task: preserve collection internal symlinks during build and install, safely handle external targets, and expose tar member metadata from extraction helpers.

Status: implementation and focused tests complete. Internal file and directory links are preserved in tar and restored on install. External file links are stored as regular files; unsafe tar links are materialized from archive content when available, or rejected if no content exists. Directory links are not traversed by the manifest walk. Path containment and extraction helper metadata are covered by tests.

Verification: `PYTHONPATH=lib:test pytest -q test/units/galaxy` passed (154 tests). `git diff --check` passed.

Final changed files: `lib/ansible/galaxy/collection.py`, `test/units/galaxy/test_collection.py`, and `changelogs/fragments/galaxy-collection-symlinks.yaml`.

Constraints: local code and tests only; no git history, index, or harness changes.
