# Checkpoint

Task: Add ipset set-extension support to the Ansible iptables module through `match_set` and `match_set_flags`.

Implemented:
- Added documented module options, including the four accepted flag values and the inversion convention (`match_set: '!name'`).
- Enforced that `match_set` and `match_set_flags` are supplied together.
- Emit `-m set` automatically when the user does not list the set match, avoid duplicating it when they do, and emit the set name/flags with `--match-set`.
- Added an ipset usage example, a changelog fragment, and unit cases for explicit/implicit matching, inversion, valid flag values, and invalid configurations.

Verification: `./bin/ansible-test units --local test/units/modules/test_iptables.py` passed (26 tests, Python 3.9). The runner skipped unavailable Python 2.6/2.7 and Python 3.5-3.8 interpreters.
