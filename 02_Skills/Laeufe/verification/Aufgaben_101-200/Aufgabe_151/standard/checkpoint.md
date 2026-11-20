# Checkpoint

Task: Fix missing JPG extensions in restricted Qt WebEngine file pickers.

Changes:
- Added `extra_suffixes_workaround` in `qutebrowser/browser/webengine/webview.py`. It uses runtime Qt version checks, `mimetypes.guess_all_extensions` for specific MIME types, and `mimetypes.types_map` for wildcards; existing suffixes are removed from the result.
- `WebEnginePage.chooseFiles` appends missing suffixes to the accepted types passed to Qt's picker, including its fallback path.
- Added focused tests for version boundaries, specific MIME types, wildcard types, already accepted suffixes, and the real local JPEG MIME mapping.

Verification:
- `python -m pytest -q tests/unit/browser/webengine/test_webview.py`: exit 0, 12 passed.
- `git diff --check`: exit 0.
- `python -m compileall -q qutebrowser/browser/webengine/webview.py tests/unit/browser/webengine/test_webview.py`: exit 0.

Local tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used grep/find instead.
