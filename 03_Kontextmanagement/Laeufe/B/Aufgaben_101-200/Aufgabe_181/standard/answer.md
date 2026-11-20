Updated [GUIProcess](/app/qutebrowser/misc/guiprocess.py) to include the correct PID in finish messages, name crash signals, and suppress SIGTERM errors unless verbose mode is enabled. Updated the [focused tests](/app/tests/unit/misc/test_guiprocess.py).

Syntax and diff checks pass. The pytest run could not collect tests because `PyQt5` is unavailable in this checkout.