Updated `getLastPersistedLocalID` to return a number or `null`, accept only numeric session keys, and leave localStorage untouched. The public bookmark flow now calls `resumeSession` only when a persisted ID exists, preserving restoration for valid sessions, including ID `0`.

The focused Jest suite passed: 13 tests. `git diff --check` passed.