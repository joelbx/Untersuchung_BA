Fixed the Qt 6.4 dark mode mapping. A numeric `colors.webpage.darkmode.threshold.text` value now produces `("ForegroundBrightnessThreshold", "100")` on Qt 6.4 and later. Earlier Qt versions retain their existing key.

Added version-specific regression coverage. All 42 dark mode tests pass with `QT_QPA_PLATFORM=offscreen`; `git diff --check` also passes.