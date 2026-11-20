# Checkpoint

Task: Fix dark mode foreground threshold option and QtWebEngine 6.4 key selection.

Initial search attempted with `rg`; unavailable (`/bin/bash: rg: command not found`). Using local `grep` and `find`.

Verification pending.

Initial test command: `python3 -m pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configdata.py tests/unit/config/test_configfiles.py` exited 134: Qt aborted in pytest-qt `qapp` fixture (headless display unavailable). Retrying with `QT_QPA_PLATFORM=offscreen`.

Implemented:
- Added public `colors.webpage.darkmode.threshold.foreground` (Int, default 256), with `threshold.text` migration and setter compatibility for existing config.py / command settings.
- Selects `TextBrightnessThreshold` before WebEngine 6.4 and `ForegroundBrightnessThreshold` at 6.4+.
- Regenerated `doc/help/settings.asciidoc` and added tests for version selection, old name assignment, and YAML migration.

Final verification:
- `QT_QPA_PLATFORM=offscreen python3 -m pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_config.py tests/unit/config/test_configdata.py tests/unit/config/test_configfiles.py` exited 0: 439 passed, 1 skipped.
- `git diff --check` exited 0.
- Documentation regeneration command exited 0: `QT_QPA_PLATFORM=offscreen python3 -c 'from scripts.dev import src2asciidoc; from qutebrowser.config import configdata; configdata.init(); src2asciidoc.generate_settings("doc/help/settings.asciidoc")'`.

Environment has QtWebEngine 5.15.2. WebEngine 6.4+ behavior is verified through version simulation and generated switch assertions, not a 6.4 runtime render.
