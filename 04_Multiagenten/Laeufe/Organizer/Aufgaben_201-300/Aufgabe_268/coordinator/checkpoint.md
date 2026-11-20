Task: Fix process error messages in qutebrowser/misc/guiprocess.py.
Status: Complete. Error-code-specific messages include capitalized process name, quoted command, and Qt detail. FailedToStart gets a Unix hint for missing or nonexecutable commands, including Qt's execvp prefix.
Verification: pytest -q --tb=short tests/unit/misc/test_guiprocess.py (30 passed); git diff --check passed.
Delegation: None.
