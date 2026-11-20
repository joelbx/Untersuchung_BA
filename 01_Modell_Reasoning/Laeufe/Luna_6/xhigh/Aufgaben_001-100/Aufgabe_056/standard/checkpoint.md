# Checkpoint

Task: Add Safari 17+ capability-aware HEIC/JXL image support and simplify MIME detection in `/app`.

Constraints: Used repository code and existing tests only; did not alter git history, index baseline, or harness configuration.

Status: Implemented in shared MIME/image support and both Drive parser copies. Existing Drive media tests passed in both `@proton/drive-store` and `proton-drive` (2 suites, 6 tests per workspace). Final diff check in progress.
