# Checkpoint

Task: Make `GUIProcess` stream stderr live and issue ordered, per-stream final summaries only for streams with output.

Progress: Connected stream-specific QProcess signals, routed live output through per-stream accumulation and severity, and used separate replacement IDs for stdout and stderr. Final summaries remain ordered stdout then stderr and are emitted only for nonempty streams. Added tests for live stderr before exit, per-stream final ordering, and line/CR handling on both streams.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find`.

Checks:
- Initial `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/misc/test_guiprocess.py` failed because newly added stderr tests did not allow the expected `message.error` log in the suite's log guard. Test contexts were corrected.
- `QT_QPA_PLATFORM=offscreen pytest -q -o addopts= tests/unit/misc/test_guiprocess.py`: 46 passed.
- `QT_QPA_PLATFORM=offscreen pytest -q -o addopts= tests/unit/misc/test_editor.py tests/unit/commands/test_userscripts.py`: 65 passed, 4 skipped.
- `git diff --check`: passed.
