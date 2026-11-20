# Checkpoint

Task: Fix Qute browser process completion messages and SIGTERM state handling.

Implemented `ProcessOutcome.was_sigterm()`, signal-aware outcome text, the `terminated` state, and completion messages that include the finishing process PID. SIGTERM completion messages are suppressed unless verbose mode is enabled. Updated existing message expectations.

Validation: `py_compile` and `git diff --check` pass. The focused pytest module could not start because PyQt5 is unavailable (`ModuleNotFoundError`).
