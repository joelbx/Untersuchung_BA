Updated the prompt reader so a canceled password read restores the terminal immediately and leaves the reader ready for a clean read. `Close` also restores an active password prompt. Added `NotifyExit` to close the shared stdin reader, and wired it into `tsh` exit handling.

Validation passed: prompt tests, prompt race tests, `tsh` package compilation, and `git diff --check`.