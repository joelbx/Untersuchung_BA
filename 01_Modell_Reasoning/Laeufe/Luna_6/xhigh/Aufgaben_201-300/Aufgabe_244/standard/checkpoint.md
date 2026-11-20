# Checkpoint

## Objective
Fix the dark mode foreground brightness threshold option and map it to the correct QtWebEngine setting key by detected version, while retaining the legacy `threshold.text` setting as an alias.

## Completed
- Added public `colors.webpage.darkmode.threshold.foreground` as an integer option with default 256.
- Declared `colors.webpage.darkmode.threshold.text` as a renamed-option migration to the new foreground option.
- QtWebEngine before 6.4 emits `TextBrightnessThreshold`; QtWebEngine 6.4+ emits `ForegroundBrightnessThreshold`.
- Regenerated `doc/help/settings.asciidoc` and added coverage for version selection, backend keys, and saved-config migration.

## Verification
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configfiles.py`: 269 passed, 1 skipped.
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_configdata.py`: 31 passed.
- `git diff --check`: passed.
