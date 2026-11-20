# Checkpoint

Task: add ipset set-extension support to the Ansible iptables module with paired `match_set` and `match_set_flags`, including tests.

Status: complete. Added documented options and example, required-together and flag-choice validation, automatic or explicit `-m set --match-set` construction, and `!` inversion support. Added unit tests for both match paths, all flags, validation, and check/append commands.

Verification: `PYTHONPATH=lib:test python -m pytest test/units/modules/test_iptables.py -q` (26 passed); `git diff --check` passed.
