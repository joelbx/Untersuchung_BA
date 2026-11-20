# Checkpoint

Task: Make GUIProcess stream stdout and stderr live, then report nonempty stdout before nonempty stderr with correct severity.

Status: implemented in qutebrowser/misc/guiprocess.py. Added a live dual-stream test and updated completion assertions in tests/unit/misc/test_guiprocess.py. The focused suite passed (41 tests, no reruns); git diff --check passed.
