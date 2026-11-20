Fixed the dark mode foreground threshold. `colors.webpage.darkmode.threshold.foreground` is now an Int option with default `256`; existing `threshold.text` settings map to it. The backend emits `TextBrightnessThreshold` before QtWebEngine 6.4 and `ForegroundBrightnessThreshold` from 6.4 onward.

Relevant tests: **436 passed, 1 skipped**.