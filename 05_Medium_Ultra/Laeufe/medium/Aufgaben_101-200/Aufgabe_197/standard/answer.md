Updated the Qt 6.4 dark mode mapping so `colors.webpage.darkmode.threshold.text = 100` emits `("ForegroundBrightnessThreshold", "100")`. Earlier Qt versions retain their existing key. Added regression coverage for both mappings.

The dark mode test file passes: 40 tests.