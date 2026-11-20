# Checkpoint

Implemented a Qt 6.4 dark mode variant in `qutebrowser/browser/webengine/darkmode.py`. It selects the `ForegroundBrightnessThreshold` key for the text threshold while preserving the Qt 6.3 and earlier mapping. Added focused key/value and version-selection tests.

Validation: the focused pytest module aborts during Qt application fixture initialization both directly and under `xvfb-run`, before tests execute.
