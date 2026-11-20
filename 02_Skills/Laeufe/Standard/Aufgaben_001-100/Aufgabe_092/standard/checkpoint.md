# Checkpoint

Implemented `ansible-galaxy collection install -U/--upgrade` and passed it through to `install_collections`. Upgrade resolution selects the newest compatible requested version, keeps installed dependencies when they satisfy constraints, replaces incompatible transitive dependencies only with upgrade enabled, and honors `--pre`, `--no-deps`, and version constraints. Install skips an already installed matching version. Added unit coverage and `test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml`.

Checks:
- `ANSIBLE_DEVEL_WARNING=False PYTHONPATH=lib:test pytest -q --reruns=0 test/units/galaxy/test_collection_install.py test/units/cli/test_galaxy.py` — 158 passed, 1 external PyYAML deprecation warning.
- `python -c 'import yaml; p="test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml"; print(len(yaml.safe_load(open(p))))'` — parsed 14 tasks.
- `git diff --check` — passed.

Earlier check `PYTHONPATH=lib:test pytest -q --reruns=0 test/units/galaxy/test_collection_install.py test/units/cli/test_galaxy.py` had four existing CLI warning-count failures caused by the development-version warning (`ANSIBLE_DEVEL_WARNING`); rerunning with that warning disabled passed. Initial patch-placement mistakes were fixed before final checks. Integration tasks require local Galaxy/Pulp services and were not executed here; their runtime behavior remains unverified.

No downloads or external research used. `rg` was unavailable, so searches used `grep` and `find`.
