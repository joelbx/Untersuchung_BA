Implemented the manifest absence handling in [collection/__init__.py](/app/lib/ansible/galaxy/collection/__init__.py) and [concrete_artifact_manager.py](/app/lib/ansible/galaxy/collection/concrete_artifact_manager.py).

An omitted `manifest` now uses `Sentinel`; explicit `manifest: null` becomes an empty configuration. The files manifest walk still applies separate ignore patterns and preserves its existing symlink handling.

Validation: `python -m pytest -q test/units/galaxy/test_collection.py` — 62 passed.