# Checkpoint

Implemented a dedicated Qt 6.4 dark mode variant. It preserves the Qt 6.3 definition except that `threshold.text` now emits `ForegroundBrightnessThreshold`; the variant selector and preferred color scheme mapping recognize Qt 6.4. Added unit coverage for emitted key/value and variant detection.

Validation: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py` passed (39 tests). A first run without offscreen mode aborted while creating the Qt application due to the headless environment.
