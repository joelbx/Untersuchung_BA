# Checkpoint

Task: replace deprecated `:buffer` with `:tab-select` throughout the command, completion, documentation, and configuration surfaces.

Initial state: repository at `/app`; `rg` is unavailable (`/bin/bash: rg: command not found`), so searches will use local `grep`/`find`.

Status: implementation complete. `CommandDispatcher.tab_select` is registered as `tab-select`; public completion providers are `tabs` and `other_tabs`; default `gt` binding, generated help, and active tests/examples use `tab-select`. Historical changelog entries remain historical.

Checks:
- `python3 scripts/dev/src2asciidoc.py` passed.
- `xvfb-run -a python3 -m pytest -p no:xvfb -q tests/unit/completion/test_models.py -k 'tab_completion or other_tabs_completion or command_completion'`: 7 passed.
- `xvfb-run -a python3 -m pytest -p no:xvfb -q tests/unit/config/test_configdata.py tests/unit/commands/test_runners.py`: 189 passed, 1 skipped.
- `QTWEBENGINE_DISABLE_SANDBOX=1 xvfb-run -a python3 -m pytest -p no:xvfb --qute-bdd-webengine -q tests/end2end/features/test_tabs_bdd.py -k tabselect --maxfail=1 --tb=short`: 13 passed, 1 skipped (preexisting flaky skip).
- `QTWEBENGINE_DISABLE_SANDBOX=1 xvfb-run -a python3 -m pytest -p no:xvfb --qute-bdd-webengine -q tests/end2end/features/test_completion_bdd.py -k 'deleting_an_open_tab or go_to_tab_after_moving_a_tab' --maxfail=1 --tb=short`: 2 passed.
- Loader registry assertion: `tab-select` registered, `buffer` absent. `git diff --check` passed.

Earlier failed checks and resolution:
- `python3 -m pytest -q tests/unit/completion/test_models.py`: 73 tests passed, but process exited 1 after `The X11 connection broke: I/O error (code 1)`. Targeted tests were rerun successfully under `xvfb-run`.
- `QT_QPA_PLATFORM=offscreen python3 -m pytest -p no:xvfb -q tests/unit/completion/test_models.py -k 'tab_completion or other_tabs_completion or command_completion' tests/unit/config/test_configdata.py`: failed at setup with `Exception: No display and no Xvfb available!`; rerun under `xvfb-run` passed.
- End to end run without `--qute-bdd-webengine` failed startup because QtWebKit cannot be imported; QtWebEngine run passed.
- An initial new count scenario used `:2tab-select` and timed out; changed to the suite's `:tab-select title.html with count 2` syntax, then passed.
- An ad hoc import of `miscmodels` before component loading hit a circular import (`AbstractWebInspector`); registry assertion after component loading passed.

No remaining known test uncertainty for the changed behavior.
