# Checkpoint

Task: Fix dark mode foreground threshold mapping across QtWebEngine versions.

Status: Investigating root cause. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find instead.

Root cause: `configdata.yml` exposes only `threshold.text`; every darkmode definition reads that name and emits `TextBrightnessThreshold`. `_variant` groups all QtWebEngine >= 6.3 together, so no 6.4 key switch exists. Existing renamed-option handling in `configdata.yml` and `YamlMigrations._migrate_configdata` can migrate saved `threshold.text` values.

Hypothesis: Rename the public option to `threshold.foreground`, declare `threshold.text` as a config migration, and add a 6.4 definition selected by `_variant`. This should preserve old WebEngine keys and emit `ForegroundBrightnessThreshold` on 6.4+.

Baseline check: `python -m pytest -q tests/unit/browser/webengine/test_darkmode.py` aborted (exit 134) while creating pytest-qt's QApplication, before running tests. Will retry with `QT_QPA_PLATFORM=offscreen`.

Implementation: `threshold.foreground` is the public Int option (default 256); `threshold.text` is a renamed option in configdata, so saved autoconfig values migrate. Darkmode definitions use `TextBrightnessThreshold` before 6.4 and a new 6.4 variant uses `ForegroundBrightnessThreshold`. Regenerated the settings reference.

Verification:
- Before fix, `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/webengine/test_darkmode.py -k 'foreground_threshold'` failed 6/6 as expected because the option was missing.
- After fix, `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_configfiles.py tests/unit/browser/webengine/test_darkmode.py`: 273 passed, 1 skipped (exit 0).
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_configdata.py tests/unit/config/test_config.py`: 162 passed (exit 0).
- `git diff --check`: passed (exit 0).

Limit: Installed WebEngine is 5.15.2. QtWebEngine 6.4+ behavior was checked with version simulation in unit tests; rendering on a 6.4+ runtime was not available locally.
