# Progress checkpoint

Task: replace deprecated `:buffer` with `:tab-select` across command registration, completion, current help, and default binding.

Status: complete. Renamed command and completion providers (`tabs`, `other_tabs`), updated current help and default `gt` binding, migrated affected scenarios, and added registration, URL, and count precedence coverage.

Verification:
- `xvfb-run -a pytest -q -p no:xvfb tests/unit/completion/test_models.py tests/unit/completion/test_completer.py -k 'not benchmark'`: 154 passed, 1 xfailed, 1 deselected.
- `QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q --qute-bdd-webengine tests/end2end/features/test_tabs_bdd.py -k tabselect --maxfail=1`: 13 passed, 1 skipped.
- `QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q --qute-bdd-webengine tests/end2end/features/test_completion_bdd.py -k 'deleting_an_open_tab or go_to_tab_after_moving_a_tab' --maxfail=1`: 2 passed.
- `git diff --check`: clean.
