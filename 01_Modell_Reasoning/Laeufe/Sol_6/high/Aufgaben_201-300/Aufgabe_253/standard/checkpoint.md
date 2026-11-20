Task: Fix GUIProcess live stderr reporting and final per-stream summaries.
Status: Complete. GUIProcess listens to separate stdout/stderr ready signals, accumulates each stream, reports live stderr as errors, and emits ordered nonempty final summaries (stdout info, stderr error). Existing CR line handling is retained for batched reads.
Tests: QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' tests/unit/misc/test_guiprocess.py (46 passed); git diff --check passed.
Changed files: qutebrowser/misc/guiprocess.py, tests/unit/misc/test_guiprocess.py.
