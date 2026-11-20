# Checkpoint

Task: Fix Bash terminal state after canceled or completed `tsh login` password prompts.

Plan: Inspect the local prompt reader and existing tests, implement terminal restoration and `NotifyExit`, then run relevant existing tests. External research and downloads are excluded.

Status: Complete. Reader cancellation and close restore the saved terminal state; `NotifyExit` closes the global stdin reader, and `tsh` calls it before exiting. Added focused tests for cancellation, deadlines, restoration errors, close, and exit notification. The prompt package tests, race check, and `tsh` compile check pass.
