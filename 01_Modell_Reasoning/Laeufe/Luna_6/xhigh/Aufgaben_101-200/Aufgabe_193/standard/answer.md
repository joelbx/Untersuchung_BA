Implemented unified requirements installs in [galaxy.py](/app/lib/ansible/cli/galaxy.py:974): bare `ansible-galaxy install -r` installs roles and collections at their default paths. Explicit subcommands and custom role paths skip the other requirement type with the requested messages. Empty requirements files now report “Skipping install, no requirements found,” and role installs display a start message.

Added routing and messaging coverage in [test_galaxy.py](/app/test/units/cli/test_galaxy.py:1160).

Verification: **153 tests passed** across the Galaxy CLI and collection install unit suites. `git diff --check` is clean.