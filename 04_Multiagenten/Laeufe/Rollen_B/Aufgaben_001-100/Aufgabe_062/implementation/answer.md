Fixed terminal restoration for abandoned password reads. `ContextReader` now restores the saved terminal state on cancellation or close, returns restoration errors, and leaves a canceled read ready for subsequent reads. Added `NotifyExit` and wired `tsh` to call it before exiting.

Verification passed: prompt tests, prompt race tests, and a `tsh` package compile.