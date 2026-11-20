# Checkpoint

Task: unify ansible-galaxy requirements installs for roles and collections.

Changed `lib/ansible/cli/galaxy.py` to retain whether the role subcommand was implicit, dispatch mixed requirements to both installers when using default paths, report skipped types, initialize parser defaults, and skip empty files. Added five regression tests in `test/units/cli/test_galaxy_unified_install.py`.

Verification:
- `PYTHONPATH=lib:test pytest -q --reruns 0 test/units/cli/test_galaxy_unified_install.py`: 5 passed.
- `ANSIBLE_DEVEL_WARNING=False PYTHONPATH=lib:test pytest -q --reruns 0 test/units/cli/test_galaxy_unified_install.py test/units/cli/test_galaxy.py test/units/cli/galaxy`: 131 passed.
- `PYTHONPATH=lib:test pytest -q --reruns 0 test/units/cli/test_galaxy_unified_install.py test/units/cli/test_galaxy.py`: 4 failures in existing collection tests due to the startup development-version warning adding an extra `Display.warning` call; targeted run passes when that warning is disabled.
- `ANSIBLE_DEVEL_WARNING=False PYTHONPATH=lib:test pytest -q --reruns 0`: 3091 passed, 22 skipped, 52 failed, 82 errors. The broad run includes unrelated collection/setup failures (including `test/units/cli/test_adhoc.py`, `test/units/config/manager/test_find_ini_config_file.py`, and integration test collection). Output was truncated, so the exact full list of failing test names is unavailable from this run. No claim of full-suite pass.
- `git diff --check`: passed.
