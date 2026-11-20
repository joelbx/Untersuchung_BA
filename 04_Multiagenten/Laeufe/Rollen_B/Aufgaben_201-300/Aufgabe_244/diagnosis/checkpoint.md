# Fault localization checkpoint

Status: diagnosis complete; no project source or tests changed.

- `qutebrowser/config/configdata.yml` defines only `colors.webpage.darkmode.threshold.text` (Int 0..256, default 256). No `threshold.foreground` option exists.
- `qutebrowser/browser/webengine/darkmode.py` maps `threshold.text` to `TextBrightnessThreshold` for both 5.15.2 and 5.15.3+ definitions. The `qt_63` definition inherits the latter; `_variant` selects `qt_63` for every WebEngine >=6.3, so 6.4 also emits the old Chromium key.
- Renamed-only YAML entries become `MIGRATIONS.renamed` in `configdata.py`; `configfiles.YamlMigrations._migrate_configdata` applies them to autoconfig.yml. `config.Config.get_opt` rejects renamed keys for direct config.py/API settings with a rename hint. Scope of requested compatibility across config.py versus autoconfig.yml needs explicit handling.
- Existing darkmode test covers only `threshold.text` -> `TextBrightnessThreshold` for 5.15.2, with no 6.4 boundary coverage.
- Attempted `pytest -q tests/unit/browser/webengine/test_darkmode.py`; runtime aborted during pytest-qt qapp fixture before test assertions (Qt runtime 5.15.2). No result on behavior.
