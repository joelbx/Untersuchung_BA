Implemented the foreground threshold option with default `256`, and mapped the legacy `threshold.text` setting to it for compatibility. Dark mode now emits `TextBrightnessThreshold` before QtWebEngine 6.4 and `ForegroundBrightnessThreshold` from 6.4 onward.

Relevant tests passed: **297 passed, 1 skipped**. `git diff --check` passed.