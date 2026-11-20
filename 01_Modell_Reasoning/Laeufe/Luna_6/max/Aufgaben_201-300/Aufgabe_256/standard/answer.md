Fixed `Play.load` so it no longer derives or mutates `name`. `get_name` now derives the name from hosts dynamically, and `_validate_hosts` raises the requested parser errors when `hosts` is present but invalid. The existing empty-hosts integration assertion now matches the new message.

Validation passed: 313 playbook, CLI, and collection-loader unit tests; the existing empty-hosts playbook produced the expected parser error; `git diff --check` passed.

Changes are in [play.py](/app/lib/ansible/playbook/play.py), [collection_loader/__init__.py](/app/lib/ansible/utils/collection_loader/__init__.py), and [runme.sh](/app/test/integration/targets/playbook/runme.sh).