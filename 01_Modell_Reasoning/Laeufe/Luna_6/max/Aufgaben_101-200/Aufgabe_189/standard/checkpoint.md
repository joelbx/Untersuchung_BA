# Checkpoint

Task: Move MIME suffix workaround into a reusable module-level helper in `qutebrowser/browser/webengine/webview.py`, update `WebEnginePage.chooseFiles`, and run relevant existing tests.

Constraints: Use repository code and existing tests only; do not request downloads or delegate. Do not change git history, index baseline, or harness configuration. Do not read credentials, private process files, benchmark solutions, or evaluator artifacts.

Progress:
- Recorded the initial checkpoint.
- Moved `extra_suffixes_workaround` to module scope with an explicit iterable input and set return type.
- Kept the Qt version gate before MIME input processing; wildcard patterns expand through `mimetypes.types_map` and results exclude requested suffixes.
- Updated `chooseFiles` to build a deduplicated union and pass it as the third positional argument to its single superclass fallback call, without using instance attributes.
- Updated existing webview tests for the module-level helper and `None` self invocation.
- Validation: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py` passed (20 tests).
