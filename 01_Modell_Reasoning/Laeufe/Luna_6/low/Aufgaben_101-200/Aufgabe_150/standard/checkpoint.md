# Checkpoint

Implemented explicit `Sentinel` handling for collection file manifests. Omitted, `None`, and empty manifest controls use the walk builder, so they produce the standard format 1 manifest and preserve separate build ignore patterns. Nonempty controls continue to use distlib and remain mutually exclusive with build ignore.

The existing walk builder excludes directory symlinks whose targets are outside the collection and records internal directory symlinks under the linked path once.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/galaxy/test_collection.py` — 66 passed.
