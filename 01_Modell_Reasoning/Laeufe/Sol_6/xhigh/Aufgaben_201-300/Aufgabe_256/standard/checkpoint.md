# Checkpoint

Task: Fix malformed Play hosts values to raise AnsibleParserError and derive the play name dynamically.

Completed:
- Moved fallback name derivation from Play.load to Play.get_name.
- Added _validate_hosts, gated on the original dataset containing hosts, with the required error messages.
- Re-exported the existing is_sequence helper through ansible.utils.collection_loader for Play to use.
- Updated the existing empty-hosts integration expectation and added Play unit regression cases.

Verification:
- PYTHONPATH=lib:test pytest -q test/units/playbook: 247 passed.
- CLI syntax check of empty_hosts.yml: expected parser error with source location.
- CLI syntax check of the reported list containing a mapping: expected invalid-host parser error with source location.
- git diff --check: clean.
