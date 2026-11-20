Updated process finish messages to include the process’s own PID. SIGTERM now has a `terminated` state and produces a finish message only in verbose mode; other signal crashes name the signal. Updated the relevant tests.

Syntax and diff checks pass. The test suite could not collect because PyQt5 is not installed locally.