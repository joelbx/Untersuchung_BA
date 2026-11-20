Updated [`guiprocess.py`](/app/qutebrowser/misc/guiprocess.py) to identify each required process error type. Failed starts now include the capitalized process name, exact command, error detail, and the non-Windows hint for missing or non-executable commands.

Updated the startup error test to check the message and hint. **Verification:** `tests/unit/misc/test_guiprocess.py` passed (21 tests).