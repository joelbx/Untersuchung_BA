# Checkpoint

Task: replace deprecated `:buffer` with `:tab-select` across command registration, completion, documentation, and examples.

Initial state: worktree clean (`git status --short` produced no entries). `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find for inspection.

Verification pending.

## Implementation

Renamed the registered tab-selection command to `tab-select`, renamed completion providers to `tabs`/`other_tabs`, updated consumers, default binding, help, manual example, and affected tests. Existing tab-selection behavior is retained; new end-to-end scenarios cover numeric index, URL substring, and count precedence. Historical changelog entries remain historical.

## Verification

- `xvfb-run -a python -m pytest -p no:xvfb -q tests/unit/completion/test_models.py`: exit 0, 73 passed.
- `QTWEBENGINE_DISABLE_SANDBOX=1 xvfb-run -a python -m pytest -p no:xvfb --qute-bdd-webengine -q tests/end2end/features/test_tabs_bdd.py -k tabselect`: exit 0, 14 passed, 1 skipped.
- `QTWEBENGINE_DISABLE_SANDBOX=1 xvfb-run -a python -m pytest -p no:xvfb --qute-bdd-webengine -q tests/end2end/features/test_completion_bdd.py -k 'deleting_an_open_tab or go_to_tab_after_moving_a_tab'`: exit 0, 2 passed.
- `QTWEBENGINE_DISABLE_SANDBOX=1 xvfb-run -a python -m pytest -p no:xvfb --qute-bdd-webengine -q tests/end2end/features/test_javascript_bdd.py -k 'closing_a_js_window_twice_issue_906__qtwebengine'`: exit 0, 1 passed.
- Direct Python registry inspection: `tab-select` registered, `buffer` absent, `tab-select` not deprecated.
- `git diff --check`: exit 0. Grep in source, help, and tests found no current `:buffer` or old completion provider references.

## Local tooling limitations and failed checks

- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/completion/test_models.py`: test output reported 73 passed, but command exited 1 after `XIO: fatal IO error 0 (Success) on X server ":0"`. Reran under explicit `xvfb-run` successfully.
- `QT_QPA_PLATFORM=offscreen python -m pytest -p no:xvfb -q tests/unit/completion/test_models.py`: exit 1; 73 setup errors, `No display and no Xvfb available!` from `tests/conftest.py`. Reran under explicit `xvfb-run` successfully.
- `xvfb-run -a python -m pytest -p no:xvfb -q tests/end2end/features/test_tabs_bdd.py -k tabselect`: exit 1; 14 failed and 1 skipped because QtWebKit was unavailable (`cannot import name 'QtWebKit' from 'PyQt5'`). Reran with installed QtWebEngine successfully. QtWebKit behavior remains unverified locally.
- `xvfb-run -a python -m pytest -p no:xvfb --collect-only -q tests/end2end/features/tabs.feature tests/end2end/features/completion.feature tests/end2end/features/javascript.feature`: exit 4; feature files are not pytest targets directly. Used corresponding `test_*_bdd.py` modules.

Final verification after renaming the internal delete callback: unit completion suite rerun (73 passed, exit 0), two completion BDD scenarios rerun (2 passed, exit 0), `git diff --check` exit 0, direct command registry assertions exit 0.
