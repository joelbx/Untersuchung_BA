`GUIProcess` now shows stderr while the process is running. At completion, it publishes a final message for each nonempty stream, with stdout at info severity before stderr at error severity. Empty streams produce no messages.

The existing carriage return handling is preserved. All 46 tests in [test_guiprocess.py](/app/tests/unit/misc/test_guiprocess.py) pass, and `git diff --check` is clean.