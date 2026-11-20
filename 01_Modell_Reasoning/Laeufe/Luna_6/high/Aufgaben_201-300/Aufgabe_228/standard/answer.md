Implemented Qt-native version handling with normalized `QVersionNumber` values across runtime and compiled Qt checks, startup validation, distribution metadata, and the crash dialog.

The focused Qt utility, utility, early-init, and crash-dialog tests passed: **318 passed**. `test_version.py` reported **89 passed, 4 skipped** when excluding `TestChromiumVersion`; pytest then exited with an X11 I/O error. The full file exits during `TestChromiumVersion::test_unpatched` before producing a summary.

`git diff --check` passed.