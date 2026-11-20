# Checkpoint

Task: Fix GUIProcess live stdout/stderr reporting and final per-stream summaries.
Status: Complete.
Changes: Connected stream-specific QProcess ready signals; live stderr now uses error severity, while stdout uses info. Each nonempty stream receives one final summary, ordered stdout then stderr. Updated tests for live messages, final ordering, severity, and empty streams.
Verification: QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/misc/test_guiprocess.py --reruns 0 (41 passed); git diff --check passed.
