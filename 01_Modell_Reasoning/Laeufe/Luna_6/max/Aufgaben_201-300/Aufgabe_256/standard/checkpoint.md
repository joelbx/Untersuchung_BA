# Checkpoint

Task: fix invalid `hosts` handling in `Play`, including lazy `get_name` derivation and parser validation.

Changes made:
- Removed `name` derivation and input mutation from `Play.load`.
- Made `get_name` return an explicit name or dynamically derive one from a sequence of hosts; `None` hosts return an empty string.
- Added `_validate_hosts`, gated on `hosts` being present in the original play dataset, with the requested parser errors for empty, `None`, non-string sequence members, and unsupported values.
- Exported the existing `is_sequence` helper at `ansible.utils.collection_loader.is_sequence` and used it in `Play`.
- Updated the existing empty-hosts integration assertion to match the required message.

Verification:
- `PYTHONPATH=lib:test python -m pytest -q test/units/playbook test/units/cli/test_playbook.py test/units/utils/collection_loader/test_collection_loader.py` — 313 passed.
- Ran the existing `empty_hosts.yml` integration fixture through `bin/ansible-playbook`; it exited with the expected parser error: `Hosts list cannot be empty. Please check your playbook`.
- `git diff --check` passed.
