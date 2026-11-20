# Checkpoint

Task: move MIME suffix workaround to module scope in webview and update chooseFiles.
Status: inspecting repository. `rg` unavailable (`/bin/bash: rg: command not found`); using grep/find.
Verification: pending.

Initial verification attempt: `pytest -q tests/unit/browser/webengine/test_webview.py` exited 134 with `Fatal Python error: Aborted` in pytest-qt's `qapp` fixture after 16 tests; likely missing display platform. No pass claim from this run. Retrying with `QT_QPA_PLATFORM=offscreen`.

Implementation: `extra_suffixes_workaround` is module-level; it checks the Qt window before MIME work, handles exact and wildcard MIME types, and returns only missing suffixes. `chooseFiles` consumes it and passes a deduplicated merged list as the third positional argument to `super().chooseFiles` on passthrough paths. Tests now call the module function and cover iterable input, version bounds, deduplication, and class-style invocation with `None`.
Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py` passed: 24 tests. `git diff --check` exited 0. No remaining class-bound helper references in source/tests.
