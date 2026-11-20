# Checkpoint

Task: Improve Qt wrapper error handling and early initialization.

Status: Implemented early machinery initialization, selection-aware availability checks, a dedicated no-wrapper error, clearer selection formatting, and focused tests. `rg` is unavailable, so local grep/find equivalents were used. No external research or downloads.

Checks:
- `PYTHONPATH=. pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py`: 33 passed.
- `PYTHONPATH=. pytest -q tests/unit/utils/test_version.py -k test_version_info`: 9 passed.
- `PYTHONPATH=. pytest -q tests/unit/utils/test_version.py -x`: exit code 1 without a pytest failure summary; output stops around 70% at the real Chromium version test. The rest of that module is unverified in this environment.
- Initial `pytest -q tests/unit/test_qt_machinery.py tests/unit/misc/test_earlyinit.py tests/unit/utils/test_version.py` could not load conftest because `qutebrowser` was not on the import path; `PYTHONPATH=.` resolved that setup issue.
