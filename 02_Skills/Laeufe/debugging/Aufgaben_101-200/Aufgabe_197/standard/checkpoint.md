# Checkpoint

Task: Correct Qt 6.4 mapping for `colors.webpage.darkmode.threshold.text`.

Status: Investigating root cause. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find`. Relevant mapping is in `qutebrowser/browser/webengine/darkmode.py`, with tests in `tests/unit/browser/webengine/test_darkmode.py`.

Root cause: `_variant()` maps every QtWebEngine version >= 6.3 to `qt_63`; that definition copies the Qt 5.15.3 settings and keeps `threshold.text` mapped to `TextBrightnessThreshold`. The configured integer is converted to a string by `_Setting._value_str`, so only the version-specific key is wrong. Existing Qt 5.15.2 customization test confirms the older spelling is intentional there. Hypothesis: a Qt 6.4 variant with a replaced threshold setting yields the required key while preserving older versions.

Reproduction: Added `test_text_threshold_key` for Qt 6.3 and 6.4. Before the fix, `QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' tests/unit/browser/webengine/test_darkmode.py::test_text_threshold_key` failed for Qt 6.4: actual `('TextBrightnessThreshold', '100')`, expected `('ForegroundBrightnessThreshold', '100')`. The direct command without `QT_QPA_PLATFORM=offscreen` (`pytest -q -o addopts='' tests/unit/browser/webengine/test_darkmode.py::test_text_threshold_key`) aborted in pytest-qt's `qapp` fixture with `Fatal Python error: Aborted` (exit 134), so subsequent runs used the offscreen platform. No check remains blocked.

Fix: Introduced `qt_64` variant for QtWebEngine >= 6.4, copying the Qt 6.3 definition while replacing only `threshold.text` with `ForegroundBrightnessThreshold`. Earlier variants retain their mappings. Added version-boundary assertions.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' tests/unit/browser/webengine/test_darkmode.py` passed (40 tests). `git diff --check` passed. No downloads performed.
