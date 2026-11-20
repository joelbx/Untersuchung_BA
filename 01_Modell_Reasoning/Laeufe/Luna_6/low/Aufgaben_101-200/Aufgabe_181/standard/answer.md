Updated [guiprocess.py](/app/qutebrowser/misc/guiprocess.py) to include signal names in crash outcomes, identify SIGTERM and set its state to `terminated`, suppress non-verbose SIGTERM messages, and include the finishing process’s PID in verbose completion messages.

The existing test file could not run because PyQt5 is missing from the environment.