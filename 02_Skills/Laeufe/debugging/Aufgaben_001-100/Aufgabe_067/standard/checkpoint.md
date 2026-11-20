# Checkpoint

Task: Add `scrolling.bar=overlay` with platform/Qt gating, update boolean migration, and support `js_headers` test marker.

Status: Investigating root cause and existing tests. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find.

Root cause: configdata.yml rejects `overlay`; `_qtwebengine_args` never emits the Chromium feature flag; boolean migration maps False to `when-searching`; BDD tag handling has no `js_headers` marker. Header update code in webenginesettings.py identifies Qt 5.12 through 5.14 as broken for runtime header updates. Hypothesis: adding the option, one guarded yield in the QtWebEngine argument path, corrected migration, and a version-aware BDD marker resolves each behavior.

Implemented: `overlay` config value; gated QtWebEngine Chromium flag for Qt runtime >= 5.11 outside macOS; False migration to overlay; `js_headers` BDD marker with skip on QtWebEngine 5.12-5.14; tagged affected header scenarios. Added regression tests for option/backend/version/platform, migration, and marker behavior; debug/GPU flag assertions now tolerate flag ordering and overlay presence.

Verification: `DISPLAY=:1 QT_QPA_PLATFORM=offscreen python -m pytest --no-xvfb -q tests/unit/config/test_configinit.py -k 'not test_new_chromium' tests/unit/config/test_configfiles.py tests/end2end/test_markers.py` exited 0: 325 passed, 1 skipped, 1 deselected. `DISPLAY=:1 QT_QPA_PLATFORM=offscreen python -m pytest --no-xvfb --collect-only -q tests/end2end/features/test_misc_bdd.py` exited 0, 74 collected. `git diff --check` exited 0.

Blocked check: `DISPLAY=:1 QT_QPA_PLATFORM=offscreen python -m pytest --no-xvfb -q tests/unit/config/test_configinit.py -k test_new_chromium -s` exited 139 with a segmentation fault in webenginesettings.py:init_user_agent called by version._chromium_version. This unrelated Chromium-version test could not be verified in the local headless Qt environment; all other tests in the selected files passed.
