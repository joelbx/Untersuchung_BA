Task: Fix GUI process outcome messages, PID references, and SIGTERM handling.
Status: Implemented SIGTERM detection and terminated state, signal names for crashes, and PID-specific completion messages. Updated existing GUIProcess tests and added SIGTERM coverage.
Verification: `pytest -q tests/unit/misc/test_guiprocess.py` cannot load tests because PyQt5 is missing. Python compileall and AST parsing passed; git diff --check passed.
