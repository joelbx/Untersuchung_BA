# Checkpoint

Task: add version-aware `qt.workarounds.disable_accelerated_2d_canvas` modes.

Initial inspection: implementation is in `qutebrowser/config/qtargs.py`, schema in `qutebrowser/config/configdata.yml`, and nearby tests in `tests/unit/config/test_qtargs.py`. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use `grep`.

Status: implemented the string enum with default `auto`, added a Qt 6 / Chromium-major resolver, and passed version, namespace, and special flags into the settings argument mapper. Added integration and boundary tests.

Checks:
- `python -m pytest tests/unit/config/test_qtargs.py -q` aborted with exit code 134 while `pytestqt/plugin.py` created `qapp` (`Fatal Python error: Aborted`). It reached no assertions. The Qt platform was not configured in that attempt.
- `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py -q`: 110 passed.
- `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py -q`: 144 passed after adding explicit Chromium boundary cases.
- `git diff --check`: passed.

Uncertainty: the tests run against the installed Qt 5 runtime and simulate Qt 6 via version data and `machinery.IS_QT6`; a native Qt 6 test environment was not available here.
