# Checkpoint

Implemented the dark-mode foreground threshold rename and backend version mapping.

- Added `colors.webpage.darkmode.threshold.foreground` as the public integer option with default 256.
- Registered `threshold.text` as a config migration to `threshold.foreground`.
- Kept `TextBrightnessThreshold` below Qt WebEngine 6.4 and mapped to `ForegroundBrightnessThreshold` starting at 6.4.
- Updated generated settings documentation and focused configuration/backend coverage.
- Focused tests passed with `QT_QPA_PLATFORM=offscreen`: 298 passed, 1 skipped. A run without the offscreen platform aborted during Qt GUI initialization before tests ran.
