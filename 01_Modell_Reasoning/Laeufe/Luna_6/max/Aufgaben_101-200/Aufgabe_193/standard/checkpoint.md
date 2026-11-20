# Checkpoint

Task: unify `ansible-galaxy install -r` handling for roles and collections, including custom-path/subcommand skip messages and role requirement processing rules.

Implementation: updated `lib/ansible/cli/galaxy.py` to distinguish implicit top-level installs from explicit subcommands, parse both requirement lists, install both types with default paths, report skipped types for explicit/custom-path installs, initialize install option context defaults, handle empty requirements, and separate role/collection install helpers. Role dependencies remain queued and only get reinstalled when force behavior is requested.

Verification: `ANSIBLE_DEVEL_WARNING=false python -m pytest test/units/cli/test_galaxy.py -q` passed (107 tests); `python -m py_compile lib/ansible/cli/galaxy.py` and `git diff --check` passed.

Working tree change: `lib/ansible/cli/galaxy.py` only. No tests were added.
