Fixed the Qt 6.4 dark mode mapping. When `colors.webpage.darkmode.threshold.text` is set to `100`, Qt 6.4 and later now emit `("ForegroundBrightnessThreshold", "100")`. Earlier versions retain their existing key.

The version-specific tests pass: **42 passed**.