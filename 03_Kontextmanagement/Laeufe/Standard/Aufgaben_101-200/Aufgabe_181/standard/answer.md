Updated `GUIProcess` so completion messages point to the finished process’s PID and crashes name the signal. SIGTERM now sets the state to `terminated` and shows a completion message only in verbose mode. The relevant unit tests were updated.

Syntax compilation and `git diff --check` passed. The unit tests could not start because `PyQt5` is unavailable in this environment.