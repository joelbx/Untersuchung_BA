# Checkpoint

Goal: stream GUIProcess stdout and stderr live, then publish nonempty per-stream summaries in stdout-before-stderr order with appropriate severities.

Status: implemented separate live handlers for stdout and stderr, shared output collection, and ordered nonempty final summaries. Updated the existing output matrix test and added a test that verifies each stream reports while the child is still running.

Verification: `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/misc/test_guiprocess.py -q` passed (42 tests); `git diff --check` passed. Flake8 was unavailable in the environment (`No module named flake8`).
