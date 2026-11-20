# Checkpoint

Task: unify ansible-galaxy requirements installation for roles and collections.
Status: complete. Bare install processes both types at default paths; role and collection subcommands handle only their own type with skip messages; custom roles paths skip collections. Empty requirements skip cleanly. Role and collection installation methods are separate.
Verification: `ANSIBLE_DEVEL_WARNING=False PYTHONPATH=lib:test pytest -q test/units/cli/test_galaxy.py` passed (113 tests); `git diff --check` passed.
