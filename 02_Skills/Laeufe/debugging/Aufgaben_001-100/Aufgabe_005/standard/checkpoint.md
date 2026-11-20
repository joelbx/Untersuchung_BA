# Qt wrapper issue checkpoint

Status: investigating root cause before edits.

- Repository: /app
- `rg` is unavailable (`/bin/bash: rg: command not found`); using local alternatives.
- Next: inspect startup flow, wrapper machinery, and existing tests; reproduce failure before patching.

Root cause: explicit startup calls machinery.init(args) before early_init, then check_pyqt only tests QtCore/QtWidgets of selected wrapper. INFO lacks import outcomes. Implicit init uses default selection without importing anything. _autoselect_wrapper raises generic Error and discards collected failures. SelectionInfo always uses verbose shape. Existing tests encode old autoselect error and version string.

Hypothesis: preserve autoselection info even on total failure, probe wrappers before the early Qt checks, and route both failure paths through a dedicated ImportError containing the same info. Preserve explicit wrapper override behavior.

Implemented: early_init initializes machinery, passes returned SelectionInfo to check_qt_available, and logs current info. The checker records import outcomes, stops after a successful import, and raises NoWrapperAvailableError with the exact required prefix and blank lines when all imports fail. Implicit init autoselects, returns INFO on success, and raises the dedicated error on failure. SelectionInfo now has short/verbose forms; autoselection records exception types. check_pyqt output gains two trailing blank lines.

Verification: `python -m pytest -q -o reruns=0 tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py tests/unit/test_qutebrowser.py tests/unit/utils/test_version.py::test_version_info` passed (63 tests). `git diff --check` passed.
