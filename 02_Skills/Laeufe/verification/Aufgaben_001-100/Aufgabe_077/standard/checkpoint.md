# Checkpoint

Task: Support module deprecation by date in Python and C#.

Implementation: updated Python warning collection, AnsibleModule exit handling, argument aliases and removed_at_date, Display date text, C# DateTime deprecation overload, C# alias validation, and validate-modules schema/date checks. Added Python and PowerShell regression coverage.

Verification:
- `PYTEST_ADDOPTS='' PYTHONPATH=lib pytest -q --forked test/units/module_utils/common/warnings/test_deprecate.py test/units/module_utils/basic/test_deprecate_warn.py test/units/module_utils/basic/test_argument_spec.py test/units/utils/display/test_display.py test/units/utils/display/test_warning.py test/units/plugins/callback/test_callback.py`: 131 passed in 3.21s.
- `git diff --check`: exit 0.
- `python -m compileall -q lib/ansible/module_utils/common/warnings.py lib/ansible/module_utils/common/parameters.py lib/ansible/module_utils/basic.py lib/ansible/utils/display.py test/lib/ansible_test/_data/sanity/validate-modules/validate_modules/main.py test/lib/ansible_test/_data/sanity/validate-modules/validate_modules/schema.py`: exit 0.

Unavailable checks and uncertainty:
- `PYTHONPATH=lib:test/lib/ansible_test/_data/sanity/validate-modules python -c 'from validate_modules.schema import argument_spec_schema; s=argument_spec_schema(); s({"x":{"removed_at_date":"2030-12-31","deprecated_aliases":[{"name":"old","date":"2030-12-31"}]}}); print("schema accepted date")'` failed with `ModuleNotFoundError: No module named 'voluptuous'`; schema runtime behavior remains unverified.
- `command -v pwsh` and `command -v dotnet` returned no paths; PowerShell integration and C# compilation remain unverified.
- `rg` unavailable (`/bin/bash: rg: command not found`); used find/grep.
- Initial combined pytest run without `--forked` failed from existing global warning/deprecation state leaking between tests. Isolated `--forked` run passed.
