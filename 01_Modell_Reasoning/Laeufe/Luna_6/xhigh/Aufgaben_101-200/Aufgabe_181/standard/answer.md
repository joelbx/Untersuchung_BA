Updated [guiprocess.py](/app/qutebrowser/misc/guiprocess.py:100) to detect SIGTERM, report signal names for crashes, mark SIGTERM processes as `terminated`, and include the PID in finish messages. Non-verbose SIGTERM exits are silent; verbose ones show an informational message.

Updated existing message expectations in [test_guiprocess.py](/app/tests/unit/misc/test_guiprocess.py:147).

Validation: syntax compilation and `git diff --check` passed. The focused pytest module could not start because PyQt5 is missing from the environment.