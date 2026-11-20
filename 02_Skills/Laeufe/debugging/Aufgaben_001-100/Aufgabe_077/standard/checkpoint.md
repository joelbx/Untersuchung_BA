# Deprecation by date checkpoint

Status: investigating current implementation and tests.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find`/`grep` searches. No downloads or external research.

## Root cause and hypothesis

The deprecation record is constructed only with `version` in `common.warnings.deprecate`. `AnsibleModule.deprecate`, `_handle_aliases`, `_handle_no_log_values`, and `common.parameters.list_deprecations` all pass version only. `exit_json` converts supplied entries through `AnsibleModule.deprecate`, which currently ignores a mapping's date. The C# module requires alias `version`, has only a string-version `Deprecate` overload, and its spec defaults omit `removed_at_date`. The validate-modules argument schema likewise requires alias version and its version checker assumes every alias has one. This consistently reproduces the absence of a date path from spec to output.

Hypothesis: adding date as an alternative at each existing deprecation boundary, while retaining the version path, will preserve ordering and allow date records and C# date formatting. A regression test must fail before the patch.

## Implementation and verification

Added date records through Python warnings, `AnsibleModule.deprecate`, exit_json mapping handling, deprecated aliases, and `removed_at_date` parameters. C# now accepts `DateTime` deprecations, formats `yyyy-MM-dd` with invariant culture, validates alias version/date exclusivity and type, and recognizes `removed_at_date`. validate-modules schema accepts dates and checks date format and passed removal dates. Documentation and regression tests were updated.

Final checks:
- `PYTEST_ADDOPTS='' PYTHONPATH=lib pytest --forked -q test/units/module_utils/basic/test_argument_spec.py test/units/module_utils/basic/test_deprecate_warn.py test/units/module_utils/basic/test_exit_json.py test/units/module_utils/common/warnings test/units/module_utils/common/parameters/test_list_deprecations.py` — exit 0, 127 passed.
- `python -m py_compile lib/ansible/module_utils/basic.py lib/ansible/module_utils/common/warnings.py lib/ansible/module_utils/common/parameters.py test/lib/ansible_test/_data/sanity/validate-modules/validate_modules/schema.py test/lib/ansible_test/_data/sanity/validate-modules/validate_modules/main.py` — exit 0.
- `git diff --check` — exit 0.

Offline tooling limitation: `PYTHONPATH=lib:test/lib/ansible_test/_data/sanity/validate-modules python - <<'PY' ... from validate_modules.schema import argument_spec_schema ... PY` failed with `ModuleNotFoundError: No module named 'voluptuous'`. The validate-modules schema and runtime date checks compile, but could not be exercised here. `command -v dotnet; command -v pwsh; command -v mcs` returned no paths (exit 1); the C# changes could not be compiled or run in this environment. No dependencies were downloaded.

Test runner note: running the selected pytest files without `--forked` exposed the existing process-wide warnings/deprecations registry leaking between tests, so the final relevant suite used the installed per-test process isolation option. An initial `-p no:rerunfailures` attempt was blocked by environment `PYTEST_ADDOPTS=--reruns=3`; setting `PYTEST_ADDOPTS=''` resolved that runner conflict.

Final consumer audit found `CallbackBase._handle_warnings` passes deprecation dictionaries as keyword arguments to `Display.deprecated`; the date regression initially failed with `TypeError: deprecated() got an unexpected keyword argument 'date'`. Display now accepts `date` and shows the removal date. The final relevant suite including display was rerun: `PYTEST_ADDOPTS='' PYTHONPATH=lib pytest --forked -q test/units/utils/display/test_display.py test/units/module_utils/basic/test_argument_spec.py test/units/module_utils/basic/test_deprecate_warn.py test/units/module_utils/basic/test_exit_json.py test/units/module_utils/common/warnings test/units/module_utils/common/parameters/test_list_deprecations.py` — exit 0, 129 passed. The final `python -m py_compile` on all changed Python production and validator files and `git diff --check` both exited 0.
