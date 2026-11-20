Issue: Qt 6.4 text dark mode threshold emits TextBrightnessThreshold; expected ForegroundBrightnessThreshold.
Initial search: rg unavailable (/bin/bash: rg: command not found); using grep fallback. Located mapping in qutebrowser/browser/webengine/darkmode.py and related tests in tests/unit/browser/webengine/test_darkmode.py.
Status: inspecting implementation and tests; no code changes yet.
Test attempt: `pytest -q tests/unit/browser/webengine/test_darkmode.py -k text_threshold_key` exited 134, Fatal Python error: Aborted during pytest-qt qapp fixture setup (display initialization). Will retry with QT_QPA_PLATFORM=offscreen.
Patch: Added Qt 6.4 variant with ForegroundBrightnessThreshold for threshold.text, preserving Qt 6.3's TextBrightnessThreshold. Added version-specific regression coverage and variant cases.
Red test evidence: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py -k text_threshold_key` exited 1; Qt 6.4 expected ('ForegroundBrightnessThreshold', '100') but emitted ('TextBrightnessThreshold', '100'). Qt 6.3 case passed.
Final verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py` exited 0, 40 passed. `git diff --check` exited 0.
