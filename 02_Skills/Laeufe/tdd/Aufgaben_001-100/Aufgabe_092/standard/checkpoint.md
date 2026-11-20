# Checkpoint

Implemented collection install `-U`/`--upgrade`, resolver preference for newest requested versions, constraint filtering for installed candidates, and a skip for an already installed resolved version. Added unit tests and `test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml`.

Verification:
- `ANSIBLE_DEVEL_WARNING=False python -m pytest -q -o reruns=0 test/units/galaxy/test_collection_install.py test/units/cli/test_galaxy.py`: 144 passed, one third-party `_yaml` deprecation warning.
- `ANSIBLE_DEVEL_WARNING=False python -m pytest -q -o reruns=0`: attempted. Collection had 19 import errors including `ModuleNotFoundError: No module named 'ansible_test._internal'`; unrelated unit tests also failed. Interrupted after 36 failures, 27 errors. Full suite status remains unknown.
- Without `ANSIBLE_DEVEL_WARNING=False`, four existing CLI tests fail because the development-version warning adds an extra warning call to their expected count.
- `rg` is unavailable (`/bin/bash: rg: command not found`); used grep/find.

Integration suite requires local Pulp services and was not executed.
- Final relevant verification: `ANSIBLE_DEVEL_WARNING=False python -m pytest -q -o reruns=0 test/units/galaxy test/units/cli/test_galaxy.py`: 264 passed, one third-party `_yaml` deprecation warning.
- `python -c "import yaml; yaml.safe_load(open('test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml')); yaml.safe_load(open('test/integration/targets/ansible-galaxy-collection/tasks/main.yml'))" && git diff --check`: passed.
