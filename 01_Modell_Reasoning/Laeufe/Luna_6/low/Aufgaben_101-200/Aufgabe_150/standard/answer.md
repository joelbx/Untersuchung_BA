Updated [_build_files_manifest](/app/lib/ansible/galaxy/collection/__init__.py:1062) to use `Sentinel` as the default and treat `Sentinel`, `None`, and `{}` as basic walk manifests. Separate ignore patterns still apply; nonempty manifest controls retain the distlib path.

Added tests for minimal controls and ignore behavior. Existing walk logic handles outside and inside symlinks as required.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/galaxy/test_collection.py` — **66 passed**. Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).