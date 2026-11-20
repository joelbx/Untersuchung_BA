# Checkpoint

- Task: Fix `GuiProcess` live stdout/stderr output and final per-stream summaries.
- Repository: `/app`; initial working tree is clean.
- Located implementation at `qutebrowser/misc/guiprocess.py` and tests at `tests/unit/misc/test_guiprocess.py`.
- Changed `GUIProcess` to read stdout and stderr independently while output messages are enabled, show live messages with stream-specific severity/replacement keys, and publish nonempty final summaries in stdout/stderr order.
- Adjusted `MessageView` duplicate detection so identical text from different streams or severities remains visible.
- Updated the existing process tests to verify live delivery before exit, severity, final order, and empty streams; added a message view regression test for identical stream text.
- Verification: `xvfb-run -a python -m pytest -q tests/unit/misc/test_guiprocess.py tests/unit/mainwindow/test_messageview.py --maxfail=1` passed (71 tests). `git diff --check` passed. Offscreen Qt produced a display-plugin warning in widget tests; Xvfb run passed.
