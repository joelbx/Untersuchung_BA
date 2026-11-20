# Checkpoint

Task: Improve Qt wrapper early initialization, error handling, and diagnostics.

Changes: `early_init` initializes machinery and checks wrapper availability; machinery returns `SelectionInfo`, autoselects on implicit initialization, and raises `NoWrapperAvailableError` with import details when needed. SelectionInfo formatting, debug logging, and Qt checker spacing were updated. Focused tests cover these paths.

Verification: `python -m pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py tests/unit/test_qutebrowser.py tests/unit/utils/test_version.py::test_version_info -o addopts='--strict-markers --strict-config'` exited 0: 61 passed.

Broader check limitation: `python -m pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py tests/unit/utils/test_version.py tests/unit/test_qutebrowser.py -o addopts='--strict-markers --strict-config'` exited 1 without a pytest failure summary while entering `TestWebEngineVersions::test_real_chromium_version`. Excluding that test, the run again exited 1 without a summary while entering `TestChromiumVersion::test_unpatched`. Both are QtWebEngine application tests; their result is uncertain in this environment. Targeted `test_version_info` passed.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local grep/find equivalents. No downloads or external research.
