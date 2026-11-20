# Checkpoint

Task: make collection manifest configuration accept minimal values and preserve file filtering and symlink behavior when `manifest_control` is `Sentinel`.

Initial state: clean working tree. `rg` is unavailable (`/bin/bash: rg: command not found`); use local `grep` and `find` for inspection.

Implementation: absent `manifest` metadata is `Sentinel`; explicit `{}` and `null` route through manifest directives with defaults. The walker still applies `build_ignore`, includes internal links once, and excludes directory and file links outside the collection.

Verification:
- `PYTHONPATH=lib python -m pytest -q test/units/galaxy/test_collection.py test/units/galaxy/test_collection_install.py` — 124 passed, exit 0.
- `git diff --check && git status --short` — exit 0; three tracked source/test files modified.
- `PYTHONPATH=lib python -c 'import distlib, pytest; print("distlib", distlib.__version__, "pytest", pytest.__version__)'` — failed with `ModuleNotFoundError: No module named 'distlib'`. Explicit manifest routing is tested with a mocked directive builder; actual distlib manifest generation could not be checked locally.
