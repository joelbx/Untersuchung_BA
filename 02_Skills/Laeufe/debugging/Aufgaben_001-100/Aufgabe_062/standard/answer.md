Fixed terminal restoration for `tsh login`. A canceled or timed out password read now restores the terminal and leaves the reader ready for a subsequent read. `Close` restores an active password prompt and returns restoration errors; `tsh` calls the new `NotifyExit` function before exiting.

Verification passed: prompt tests, prompt race tests, the `tsh` build check, and `git diff --check`.