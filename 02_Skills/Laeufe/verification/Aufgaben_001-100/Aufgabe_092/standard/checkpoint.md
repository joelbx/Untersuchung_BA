# Checkpoint

Task: implement Ansible Galaxy collection --upgrade with constraint-aware dependency resolution and tests.

Status: implementation and local verification complete. `rg` unavailable (`/bin/bash: rg: command not found`); used `find`/`grep`.

Changes: added `-U`/`--upgrade` to collection install, propagated it through the resolver, selected the newest allowed direct request while retaining compatible installed dependencies, and skipped installation when the selected version is already present. Added unit coverage and integration tasks in `upgrade.yml` for stable, prerelease, idempotent, requirements-file, and transitive-dependency upgrades.

Verification:
- `PYTHONPATH=lib python -m pytest -q test/units/galaxy/test_collection_install.py`: 35 passed.
- `PYTHONPATH=lib python -m pytest -q test/units/galaxy/test_collection_install.py test/units/cli/test_galaxy.py`: 4 failed, 141 passed. Existing CLI tests count warnings and the development-version warning adds one; a fresh isolated CLI test reproduced both warning calls.
- `ANSIBLE_DEVEL_WARNING=False PYTHONPATH=lib python -m pytest -q test/units/galaxy/test_collection_install.py test/units/cli/test_galaxy.py`: 148 passed, 1 yaml deprecation warning.
- `python` YAML safe_load of integration `main.yml` and `upgrade.yml`: both parsed.
- Final `git diff --check` and fresh unit suite: no diff errors; 148 passed, 1 yaml deprecation warning. Final YAML parse: `main.yml` 20 tasks, `upgrade.yml` 18 tasks.

The Pulp-backed integration tasks were added but not run locally; they require the integration target's services.
