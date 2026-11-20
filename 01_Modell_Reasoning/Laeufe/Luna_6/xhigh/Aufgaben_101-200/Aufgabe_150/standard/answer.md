Implemented the manifest configuration changes.

- Missing `manifest` values now use `Sentinel`; explicit `{}` and `null` are treated as manifest configurations, with `null` using default directives.
- Missing manifests use the filesystem walker and still honor separate ignore patterns.
- Outside file symlinks are excluded. Existing handling keeps internal directory symlinks under their linked paths once.
- Updated existing walker tests to use `Sentinel` for the absent-manifest case.

Validation: `PYTHONPATH=/app/lib python3 -m pytest -q test/units/galaxy/test_collection.py` — **62 passed**. `git diff --check` passed.

Changes are in [collection manifest handling](/app/lib/ansible/galaxy/collection/__init__.py:1062) and [galaxy.yml normalization](/app/lib/ansible/galaxy/collection/concrete_artifact_manager.py:578). Explicit manifest configurations continue to require `distlib`.