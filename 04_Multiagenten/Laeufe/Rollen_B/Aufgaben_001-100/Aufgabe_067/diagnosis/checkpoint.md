# Fault localization progress

Inspected local configuration, Qt argument generation, migration, header behavior, and tests. No project source or tests changed.

- `qutebrowser/config/configdata.yml` defines `scrolling.bar` valid values at line 1488; `overlay` is absent.
- `qutebrowser/config/configinit.py` `qt_args` (line 176) appends `_qtwebengine_args` (line 286) only for QtWebEngine. The latter is the likely location for an `overlay` flag guard using `qtutils.version_check('5.11', compiled=False)` and `utils.is_mac`. Existing stylesheet logic in `qutebrowser/browser/shared.py:get_user_stylesheet` hides bars only for `never` and inactive `when-searching`, so `overlay` already falls through to visible non-overlay behavior.
- `qutebrowser/config/configfiles.py:YamlMigrations.migrate` line 322 maps `False` to `when-searching`; requirement calls for `overlay`. Existing migration expectation is at `tests/unit/config/test_configfiles.py:504`.
- `tests/unit/config/test_configinit.py:TestQtArgs` covers Qt argument generation. `test_chromium_debug` and `test_disable_gpu` at lines 539 and 545 compare whole argument lists; they need to remain order independent when an overlay flag is enabled.
- `tests/end2end/conftest.py` translates BDD tags via `_get_version_tag` and `_get_backend_tag` and applies marker skips in `pytest_collection_modifyitems`; no `js_headers` marker exists. `pytest.ini` also lacks registration. `qutebrowser/browser/webengine/webenginesettings.py:_update_settings` line 331 identifies Qt 5.12 through 5.14 as affected by a dynamic header bug, with support before 5.12 or from 5.15. Relevant BDD header scenarios are in `tests/end2end/features/misc.feature` around line 323.

Uncertainty: The issue does not spell out whether `@js_headers` should apply to all header scenarios or only those that change headers after startup; existing code suggests targeting dynamic header tests. No runtime tests were run because this role is limited to diagnosis and cannot change source/tests.
