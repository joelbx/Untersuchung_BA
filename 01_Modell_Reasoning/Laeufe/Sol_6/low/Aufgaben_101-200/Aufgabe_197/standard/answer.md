Fixed the Qt 6.4 mapping so a numeric `colors.webpage.darkmode.threshold.text` value emits `ForegroundBrightnessThreshold` as a string. Earlier Qt variants retain their existing key.

The dark mode test suite passed: 40 tests with `QT_QPA_PLATFORM=offscreen`.