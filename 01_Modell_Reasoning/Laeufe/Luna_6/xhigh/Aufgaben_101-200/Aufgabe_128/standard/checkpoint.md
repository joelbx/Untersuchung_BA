# Checkpoint

Task: Add `match_set` and `match_set_flags` support to the Ansible iptables module, including pair validation, explicit/implicit set-match behavior, inversion, and integration with other rule options.

Completed:
- Added documented `match_set` and `match_set_flags` module parameters, flag choices, and required-together validation.
- Added rule construction for implicit or declared `set` matches. A `!` prefix on the set name inverts the `--match-set` condition.
- Added an ipset example and unit coverage for all allowed flag values, explicit/implicit matches, inversion, ports/jump/comment integration, incomplete parameter pairs, and invalid flags.

Verification:
- `python -m pytest -q test/units/modules/test_iptables.py`: 25 passed.
- `python -m py_compile lib/ansible/modules/iptables.py test/units/modules/test_iptables.py`: passed.
- `git diff --check`: passed.
