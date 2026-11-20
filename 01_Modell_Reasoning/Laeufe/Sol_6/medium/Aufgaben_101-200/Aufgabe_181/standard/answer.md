Updated `GUIProcess` so completion messages name the process outcome and point to that process’s PID. SIGTERM now sets the state to `terminated` and produces a message only in verbose mode; other signal crashes name the signal. The existing unit tests were updated to cover these cases.

Syntax and diff checks passed. The unit tests could not start because PyQt5 is unavailable in this environment.