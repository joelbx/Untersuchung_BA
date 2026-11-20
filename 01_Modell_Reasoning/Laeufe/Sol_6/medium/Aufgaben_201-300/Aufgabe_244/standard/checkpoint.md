# Checkpoint

Task: Fix QtWebEngine dark mode foreground brightness threshold compatibility.

Completed: Added the foreground option (Int, default 256), migrated saved text settings, kept old config.py names working, and selected the Chromium key by WebEngine version. Regenerated the settings reference.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configfiles.py tests/unit/config/test_configdata.py tests/unit/config/test_config.py` passed (436 passed, 1 skipped). `git diff --check` passed.
