# Checkpoint

Task: support module deprecation by date.
Status: inspecting repository and preparing failing tests.

Verification obstacles:
- `pwsh -NoProfile -Command '$PSVersionTable.PSVersion'` -> `/bin/bash: pwsh: command not found`; C# integration tests cannot run here.
- `PYTHONPATH=lib:test/lib/ansible_test/_data/sanity/validate-modules pytest -q test/ansible_test/validate-modules-unit/test_deprecation_dates.py` -> collection error `ModuleNotFoundError: No module named 'voluptuous'`; schema and validate-modules behavior remains unexecuted.

Implementation: Python warning collector and AnsibleModule accept date deprecations; argument and alias deprecations propagate dates; display renders date; C# adds DateTime overload and validates alias removal targets; validate-modules schema and expired-date checks added; docs updated.

Checks:
- `PYTHONPATH=lib pytest -q --forked test/units/module_utils/common/warnings/test_deprecate.py test/units/module_utils/basic/test_deprecate_warn.py test/units/module_utils/common/parameters/test_list_deprecations.py test/units/utils/display/test_display.py` -> 23 passed.
- `python -m compileall -q lib/ansible/module_utils/basic.py lib/ansible/module_utils/common/warnings.py lib/ansible/module_utils/common/parameters.py lib/ansible/utils/display.py test/lib/ansible_test/_data/sanity/validate-modules/validate_modules/schema.py test/lib/ansible_test/_data/sanity/validate-modules/validate_modules/main.py` -> passed.
- `git diff --check` -> passed.
- `PYTHONPATH=lib pytest -q --forked test/units` -> 3233 passed, 22 skipped, 5 failed, 8 errors. Failures: test_collection_install_with_names, test_collection_install_with_requirements_file, test_collection_install_in_collection_dir, test_collection_install_path_with_ansible_collections (test/units/cli/test_galaxy.py); test_execute_list_collection_one_invalid_path (test/units/cli/galaxy/test_execute_list_collection.py). Eight setup errors in TestFindIniFile (test/units/config/manager/test_find_ini_config_file.py), all `TypeError: str expected, not NoneType`.
- `PYTHONPATH=lib pytest -q --forked --maxfail=1` -> collection stopped with `ModuleNotFoundError: No module named 'ansible_test._internal'` in test/ansible_test/unit/test_diff.py. Full project suite remains unverified.
