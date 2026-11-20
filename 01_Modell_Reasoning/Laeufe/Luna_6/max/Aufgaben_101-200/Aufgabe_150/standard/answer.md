Implemented the manifest handling changes:

- Missing `manifest` configuration now uses `Sentinel`; `{}` is handled as an explicit configuration, while `null` uses the no-manifest path.
- Ignore patterns remain active when `manifest_control` is `Sentinel`.
- The walker skips external file and directory symlinks and lists internal directory symlinks once at their linked path.
- Updated existing walker tests to use `Sentinel` for the omitted-config case.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/galaxy/test_collection.py` — **62 passed**.

Files: [collection builder](/app/lib/ansible/galaxy/collection/__init__.py), [metadata normalizer](/app/lib/ansible/galaxy/collection/concrete_artifact_manager.py), [collection tests](/app/test/units/galaxy/test_collection.py).