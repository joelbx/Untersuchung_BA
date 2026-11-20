VERDICT: FIX

The applied production changes match the requested process messages in the paths reviewed, but two new tests fail. I made no project code changes.

- [test_guiprocess.py:436](/app/tests/unit/misc/test_guiprocess.py:436): the verbose failure test expects one total message, although verbose mode also emits “Executing:”. Select the error message without assuming it is the only message.
- [test_guiprocess.py:457](/app/tests/unit/misc/test_guiprocess.py:457): the PID test does not allow the expected ERROR log. Wrap the finish wait in `caplog.at_level(logging.ERROR)`, as adjacent tests do.

**Tests:** `QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/misc/test_guiprocess.py` ran with 43 passed and 2 failed (exit 1). **TEST_ENVIRONMENT_PROBLEM:** the initial command, `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/misc/test_guiprocess.py`, could not import the checkout’s default PyQt5 (exit 4); selecting the installed PyQt6 allowed the suite to run.