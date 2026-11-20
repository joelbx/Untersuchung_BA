# Checkpoint

Task: allow minimal collection manifest configuration and preserve file selection when the manifest control is absent.

Initial state: working tree clean. The `manifest` key was normalized to `{}` when absent, and `_build_files_manifest` used truthiness to choose between the directory walk and manifest directives. The absent value now uses `Sentinel`; explicit `{}` and `null` select default manifest directives. Both manifest paths exclude symlinks that resolve outside the collection, and relative collection paths are handled in symlink checks. Documentation and unit tests were updated.

Validation: `PYTHONPATH=lib python -m pytest -q test/units/galaxy/test_collection.py test/units/galaxy/test_collection_install.py` passed (128 tests). `git diff --check` passed. The optional `distlib` dependency is unavailable locally, so its integration path was covered using the existing unit test approach with a mock `Manifest`.
