# Checkpoint

Task: Fix GUIProcess live stdout/stderr reporting and deterministic per-stream summaries.
Status: Complete.
Changes: Read stdout and stderr independently as data arrives; emit live info/error messages only for output-producing streams; drain both streams at finish and publish stdout then stderr summaries. Added tests for live messages before process exit, severity, order, and empty streams.
Verification: `python -m pytest tests/unit/misc/test_guiprocess.py tests/unit/misc/test_editor.py tests/unit/commands/test_userscripts.py -q --reruns 0` (107 passed, 4 skipped); `git diff --check` passed.
Delegation: None.
