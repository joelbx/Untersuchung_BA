Task: Fix GUIProcess finish messages and SIGTERM handling.
Status: Implemented PID-specific finish messages, signal names, and SIGTERM outcome/state with quiet nonverbose termination. Updated process tests, including a last_pid regression test.
Verification: PyQt6/offscreen process, editor, and completion suites: 173 passed, 4 skipped. Python compileall and git diff --check passed.
