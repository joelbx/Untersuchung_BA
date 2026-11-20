# Resolution

`Play.load` no longer derives or writes `name`. `Play.get_name` derives the display name from the current `hosts` value. `_validate_hosts` checks only plays whose original dataset contains `hosts`, and reports the specified parser errors for empty, `None`, invalid sequence elements, and unsupported types. The repository's `is_sequence` helper is re-exported from `ansible.utils.collection_loader` for this use.

# Checks

- `PYTHONPATH=lib:test python -m pytest -q test/units/playbook/test_play.py test/units/playbook/test_playbook.py test/units/playbook/test_collectionsearch.py`: 21 passed.
- `PYTHONPATH=lib:test python -m pytest -q test/units/playbook`: 248 passed (16 deprecation warnings from existing tests).
- `git diff --check`: passed.

`rg` is unavailable (`/bin/bash: rg: command not found`); local `grep` and `find` were used to inspect the repository.
