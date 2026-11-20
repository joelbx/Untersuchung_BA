# Checkpoint

Implemented the Qt wrapper initialization and diagnostics changes:

- `machinery.init` returns its `SelectionInfo`; implicit initialization autoselects an importable wrapper and raises `NoWrapperAvailableError` if none can be imported.
- Added `NoWrapperAvailableError`, updated `SelectionInfo` formatting, and included exception type names in autoselection failures.
- Early initialization receives the selection info, validates the selected wrapper, adds trailing blank lines to checker diagnostics, and logs the selection details.
- Updated the application startup handoff.

Verification: `PYTHONPATH=. pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py` reported 22 passed and 5 failures. The failures assert superseded behavior: the previous error text, error-only import details, and implicit initialization through `_select_wrapper`. `tests/unit/misc/test_earlyinit.py` passed. `compileall` succeeded.
