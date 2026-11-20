# Checkpoint

Task: add ipset matching support to the Ansible iptables module.

Completed:
- Added `match_set` and `match_set_flags` module options with the requested flag choices and paired validation.
- Constructed the set match automatically when the options are supplied; explicit `match: ['set']` is supported without a duplicate extension.
- Added support for `!` inversion on the set name and placed the set clause before the jump target.
- Added unit coverage for implicit and explicit set matches, inversion, common rule options, and incomplete parameter pairs.

Verification: `python -m pytest test/units/modules/test_iptables.py -q` passed (25 tests); `git diff --check` passed.
