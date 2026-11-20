# Checkpoint

- Task: restore the dark mode foreground threshold option and select its Chromium key by Qt WebEngine version.
- Started with a clean working tree. `rg` is unavailable, so repository searches will use `grep`.
- Implemented `colors.webpage.darkmode.threshold.foreground` as an Int option with default 256. Saved YAML and existing `config.py` uses of `...threshold.text` resolve to the new option.
- Dark mode settings emit `TextBrightnessThreshold` below QtWebEngine 6.4 and `ForegroundBrightnessThreshold` from 6.4 onward. Regenerated the settings reference.
- Validation: 560 passed, 1 skipped across the relevant dark mode and configuration test modules. `git diff --check` passed.
