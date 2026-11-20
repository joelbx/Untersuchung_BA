# Checkpoint

Implemented a Qt 6.4 dark mode variant that inherits the Qt 6.3 configuration and emits `ForegroundBrightnessThreshold` for `threshold.text`; older variants retain their prior key. Added a test for the serialized numeric value and variant detection.

Validation: `QTWEBENGINE_DISABLE_SANDBOX=1 QT_QPA_PLATFORM=offscreen xvfb-run -a pytest -q tests/unit/browser/webengine/test_darkmode.py` passed (39 tests). The test file aborts during Qt fixture startup without those environment settings.
