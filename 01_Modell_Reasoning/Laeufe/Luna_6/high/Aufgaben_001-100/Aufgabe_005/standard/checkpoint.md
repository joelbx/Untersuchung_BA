# Checkpoint

Task: improve early Qt wrapper initialization and diagnostics.

Implemented:
- Added `NoWrapperAvailableError` carrying `SelectionInfo` and the required leading message/blank lines.
- Made selection output concise while outcomes are incomplete and verbose once both PyQt probes are known; autoselection records exception class names.
- Made `machinery.init()` return its `SelectionInfo`; implicit initialization autoselects and raises the dedicated error if no wrapper imports.
- Moved wrapper initialization into early startup, passed its result to `check_qt_available()`, and logged the current info at debug level.
- Added the requested trailing blank lines to Qt checker diagnostics.
- Updated and added focused unit coverage.

Validation:
- `PYTHONPATH=. pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py tests/unit/utils/test_version.py::test_version_info`: 39 passed.
- The full `tests/unit/utils/test_version.py` process exited with code 1 before producing a pytest summary; its focused `test_version_info` cases passed.
- `git diff --check` passed.
