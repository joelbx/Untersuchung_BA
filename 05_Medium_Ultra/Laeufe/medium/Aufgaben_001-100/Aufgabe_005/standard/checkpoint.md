Task: Improve Qt wrapper error handling and early initialization.
Status: Implemented early machinery initialization, availability checking, the dedicated no-wrapper error, SelectionInfo formatting, clearer import failures, and debug reporting. Added focused coverage and updated the version-report expectation.
Verification: 42 focused machinery, earlyinit, and version-report tests passed. git diff --check passed. The full version test module stopped during its unrelated real Chromium check in this environment.
