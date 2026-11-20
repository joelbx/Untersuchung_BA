Fixed the Qt 6.4 dark mode mapping. A numeric `colors.webpage.darkmode.threshold.text` value now emits `("ForegroundBrightnessThreshold", "100")` for Qt 6.4; Qt 6.3 keeps its existing key.

The regression test reproduced the wrong key before the fix. After the change, all 40 dark mode tests pass, and `git diff --check` passes.