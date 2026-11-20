Task: introduce a shared QVersionNumber parser and migrate specified version checks.
Status: implementation complete. Added normalized QVersionNumber parsing and migrated Qt, distribution, startup, and crash dialog checks. Updated and added focused tests.
Verification: 343 focused tests passed using xvfb-run with the pytest xvfb plugin disabled. git diff --check passed.
Delegation: none; solved directly.
