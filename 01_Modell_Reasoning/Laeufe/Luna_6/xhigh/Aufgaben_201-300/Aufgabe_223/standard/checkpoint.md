# Checkpoint

Task: honor declared module interpreters, preserve interpreter arguments, respect explicit interpreter overrides, fall back through configured Python discovery when a module has no shebang, and place the encoding cookie directly after the shebang.

Findings:
- New style Python modules were assembled with a hard-coded `#!/usr/bin/python` wrapper line.
- `modify_module` only rewrote existing shebangs for explicit overrides, returned no shebang for modules without one, and inserted the coding cookie only for Python paths.
- `_extract_interpreter` did not exist.

Changes made:
- Added `_extract_interpreter`, Python interpreter detection, explicit Python override lookup, and shebang generation that always includes `#!` and args.
- New style wrappers preserve module shebangs unless an explicit Python override is configured; no-shebang modules continue through configured interpreter discovery.
- `modify_module` preserves original shebangs unless the resolved interpreter differs, adds a Python fallback shebang where absent, and puts the encoding cookie immediately after it.
- Added unit coverage for parsed args, versioned/env shebangs, new style modules, old style modules, overrides, and no-shebang fallback.

Validation so far: focused module-common unit tests pass (52 tests). `git diff --check` passes.

Final validation: `python -m pytest -q test/units/executor/module_common` passes all 60 tests. The suite emits one `PytestUnraisableExceptionWarning` from a `test_recursive_finder.py` case during `ZipFile` finalization. `git diff --check` passes.
