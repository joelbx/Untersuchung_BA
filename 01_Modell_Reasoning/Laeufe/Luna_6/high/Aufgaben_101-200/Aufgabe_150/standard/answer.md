Implemented flexible manifest handling in [collection/__init__.py](/app/lib/ansible/galaxy/collection/__init__.py) and [concrete_artifact_manager.py](/app/lib/ansible/galaxy/collection/concrete_artifact_manager.py).

An omitted `manifest` now uses `Sentinel`. `Sentinel`, `{}`, and `None` produce a format 1 walk-based files manifest, with separate ignore patterns applied. The walk skips symlinks that resolve outside the collection while retaining internal links under their linked paths.

Verification: `python -m pytest -q test/units/galaxy/test_collection.py` passed (62 tests); `git diff --check` passed.