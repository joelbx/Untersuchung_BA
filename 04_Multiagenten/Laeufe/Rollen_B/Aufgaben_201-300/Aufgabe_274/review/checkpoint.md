VERDICT: FIX
Code review: no correctness or regression defect found in the applied patch. The enum, default, argument routing, auto resolver, and requested version boundaries match the issue.
TEST_ENVIRONMENT_PROBLEM: `pytest -q tests/unit/config/test_qtargs.py` aborted (exit 134) in pytest-qt's qapp fixture without a Qt display. Use `QT_QPA_PLATFORM=offscreen` in this environment.
Executed: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py` -> 111 passed; `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_configdata.py` -> 31 passed. `git diff --check` passed.
The FIX verdict follows the review rule requiring FIX for any interrupted relevant test. No project-code correction is indicated; rerun relevant Qt tests with the offscreen platform.
