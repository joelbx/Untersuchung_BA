# Checkpoint

Task: Fix invalid `hosts` handling in `Play`.

Changes:
- `Play.load` no longer derives or writes `name` from `hosts`.
- `Play.get_name` derives a name from the current hosts value when no name is set.
- `_validate_hosts` checks only plays whose original dataset contains `hosts`, and reports the specified parser errors for empty, `None`, invalid sequence entries, and invalid scalar types.
- Added focused unit coverage for these cases, explicit names, input immutability, and dynamic names.

Repository note: `ansible.utils.collection_loader.is_sequence` does not exist in this checkout. The existing helper is `ansible.module_utils.common.collections.is_sequence`; it is used without adding a new public interface. `rg` is unavailable (`/bin/bash: rg: command not found`), so searches used `grep` and `find`.

Verification:
- `PYTHONPATH=lib:test python -m pytest -q --disable-warnings test/units/playbook`: exit 0, 247 passed, 16 warnings.
- `git diff --check`: exit 0.
- `PYTHONPATH=lib python bin/ansible-playbook --syntax-check -i localhost, /dev/stdin` with a play containing `hosts: [localhost, {test: value}]`: exit 4 with `ERROR! Hosts list contains an invalid host value: '{'test': 'value'}'` and a source location. This is the expected parser rejection, without an unexpected exception.
