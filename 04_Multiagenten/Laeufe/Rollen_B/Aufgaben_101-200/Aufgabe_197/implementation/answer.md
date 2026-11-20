Fixed the Qt 6.4 dark mode mapping. When `colors.webpage.darkmode.threshold.text` is set to `100`, it now emits `("ForegroundBrightnessThreshold", "100")` under `dark-mode-settings`. Earlier version mappings remain covered by the tests.

Verification: all 41 dark mode tests passed with `QT_QPA_PLATFORM=offscreen`; `git diff --check` passed.