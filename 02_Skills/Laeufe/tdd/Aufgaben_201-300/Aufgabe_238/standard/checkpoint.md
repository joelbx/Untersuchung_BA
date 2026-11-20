# Checkpoint

Issue: replace deprecated `:buffer` with `:tab-select` in command registration, completion, and user-facing documentation.

Status: inspecting repository and tests. Applying test-first changes.

Implemented: registered `tab-select` by renaming the command handler; renamed completion providers to `tabs` and `other_tabs`; updated default binding, help, examples, and feature scenarios. Existing selection logic continues to handle counts, indices, title/URL matching, cross-window focus, and qute://tabs fallback.

Test-first: changed completion tests before implementation. `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/completion/test_models.py -k 'tab_completion or other_tabs_completion or tab_select_is_in_command_completion'` failed for missing providers and command. After fixing the test fixture, the command test failed as expected with `assert 'tab-select' in []`.

Passing: `xvfb-run -a env QT_QPA_PLATFORM=offscreen pytest -q -p no:xvfb tests/unit/completion/test_models.py tests/unit/completion/test_completer.py --reruns 0` — 155 passed, 1 xfailed, exit 0.

Full-suite attempt: `timeout 180 xvfb-run -a env QT_QPA_PLATFORM=offscreen pytest -q -p no:xvfb --reruns 0` — end-to-end tests fail while starting QtWebKit: `cannot import name 'QtWebKit' from 'PyQt5'`. Those failures do not establish whether the renamed end-to-end scenarios pass. No downloads attempted.

Additional checks:
- `xvfb-run -a env QT_QPA_PLATFORM=offscreen pytest -q -p no:xvfb tests/unit/api/test_cmdutils.py tests/unit/commands tests/unit/config/test_configdata.py --reruns 0 --tb=line` — 295 passed, 1 skipped, exit 0.
- `timeout 90 xvfb-run -a env QUTE_BDD_WEBENGINE=true QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q -p no:xvfb tests/end2end/features/test_tabs_bdd.py -k tabselect --reruns 0 --tb=line` — 11 passed, 1 skipped, exit 0. Covers no args, title matching, invalid inputs, and window indices; one existing cross-window scenario is skipped as flaky.
- `timeout 60 xvfb-run -a env QUTE_BDD_WEBENGINE=true QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q -p no:xvfb tests/end2end/features/test_completion_bdd.py -k 'deleting_an_open_tab_via_the_completion or go_to_tab_after_moving_a_tab' --reruns 0 --tb=line` — 2 passed, exit 0.

Suite limitations: the broad command above reported `test_open_s[http://]` and `test_optimize[2]` among end-to-end failures because QtWebKit is missing, then was interrupted (exit 130) to avoid continuing thousands of known failures. It also reached an existing helper test that invoked pip for `wheel` and failed with `No matching distribution found for wheel`; no dependencies were downloaded. A concurrent `tests/unit` attempt exited 1 without a final summary while the broad run was being interrupted, so it does not establish unit-suite status. The focused commands above passed after that run stopped. An offscreen WebEngine BDD attempt passed its scenario but produced a teardown error (`This plugin does not support raise()`); rerunning with Xvfb's normal xcb platform passed.

Final diff check: `git diff --check` passed. Historical changelog entries were retained as historical records; current help/config/example references use `tab-select`.
