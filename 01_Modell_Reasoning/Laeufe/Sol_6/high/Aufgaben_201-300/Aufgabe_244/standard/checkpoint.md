# Checkpoint

Task: Fix QtWebEngine dark mode foreground brightness threshold option and version-specific backend key.
Status: Complete. Added foreground Int option (default 256), accepted text as a compatibility alias with YAML migration, selected Chromium key by WebEngine version, regenerated settings reference, and added regression coverage.
Verification: 438 passed, 1 skipped, 1 rerun across darkmode/config suites; final focused tests 8 passed; git diff --check passed.
