# Checkpoint

Issue: unify `ansible-galaxy install -r` handling for roles and collections, including custom path behavior and clear skip messages.

Implemented shared requirements parsing and dispatch in `lib/ansible/cli/galaxy.py`. Bare `install` installs both types at default paths; explicit subcommands and custom role paths skip the other type with the required warning or verbose message. Added role install start output, empty requirements handling, parser context defaults, extension validation, and force-aware dependency queuing.

Added unit coverage in `test/units/cli/test_galaxy.py` for mixed installs, path routing, skip messages, empty requirements, and parser defaults.

Verification so far: `PYTHONPATH=/app/lib ANSIBLE_DEVEL_WARNING=false python -m pytest -q test/units/cli/test_galaxy.py test/units/galaxy/test_collection_install.py` — 153 passed.
