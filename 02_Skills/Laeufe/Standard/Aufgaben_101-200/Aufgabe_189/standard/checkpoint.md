# Checkpoint

Task: move MIME suffix workaround to a module-level helper in `webview.py`, update `chooseFiles`, and run relevant existing tests.

Status: inspecting repository. `rg` is unavailable (`/bin/bash: rg: command not found`), so using `grep`/`find` for local search.

Initial test attempt: `python -m pytest tests/unit/browser/webengine/test_webview.py -q` exited 134 after 15 tests. Qt aborted while pytest-qt created `qapp`; test result was incomplete. Retrying with `QT_QPA_PLATFORM=offscreen`.

Implemented: moved `extra_suffixes_workaround` to module scope, preserved Qt version gating and wildcard expansion, and made `chooseFiles` forward a deduplicated union through its existing superclass paths. Updated tests to use the module helper and a `None` receiver; added version-window and one-shot iterable checks.

Verification:
- `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/browser/webengine/test_webview.py -q` — 23 passed.
- `git diff --check` — passed.
- `python -m flake8 qutebrowser/browser/webengine/webview.py tests/unit/browser/webengine/test_webview.py` — failed: `/usr/local/bin/python: No module named flake8`. Lint status remains unchecked because the tool is unavailable locally; no dependencies were downloaded.
