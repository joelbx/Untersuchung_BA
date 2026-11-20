# Checkpoint

Task: implement QtWebEngine 5.15.3 locale workaround and verify with relevant tests.

Initial repository search: `rg` unavailable (`/bin/bash: rg: command not found`); using grep/find.

Verification attempt 1: `python -m pytest tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py -q` exited 134 (Qt aborted during test setup, before assertions). Retried with `QT_QPA_PLATFORM=offscreen`.
Verification attempt 2: `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py -q --disable-warnings` exited 1: 5 new test expectations were wrong for locales with an existing exact .pak; 173 passed. Corrected those tests.

Final verification: `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py -q --disable-warnings` exited 0: 178 passed in 2.97s. `git diff --check` exited 0. Runtime is Qt 5.15.2, so the actual QtWebEngine 5.15.3 crash cannot be reproduced here; mapping and argument behavior were tested using the version stub.
