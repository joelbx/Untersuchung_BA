Updated `GUIProcess` so completion messages include the process’s own PID. SIGTERM now produces a `terminated` state and no completion message unless verbose mode is enabled; other signal crashes name the signal.

I updated the existing tests and added SIGTERM coverage. Syntax checks and `git diff --check` passed. The test suite could not start because PyQt5 is missing from this environment.