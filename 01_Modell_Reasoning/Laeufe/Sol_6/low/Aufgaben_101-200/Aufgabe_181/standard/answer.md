Updated `GUIProcess` so completion messages include the finished process’s PID. Crash messages name the signal, and SIGTERM sets the state to `terminated` without showing an error unless verbose mode is enabled. Added tests for these cases.

Syntax and diff checks passed. The relevant pytest suite could not start because PyQt5 is missing from the environment.