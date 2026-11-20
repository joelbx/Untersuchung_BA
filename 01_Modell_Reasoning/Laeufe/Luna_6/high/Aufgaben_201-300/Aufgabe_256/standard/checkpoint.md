# Checkpoint

Issue: validate malformed play `hosts` values with clear parser errors, while deriving the play name dynamically in `get_name`.

Completed:
- Removed name mutation and host joining from `Play.load`.
- Added dynamic name derivation in `get_name`, including missing/`None` hosts behavior.
- Added `_validate_hosts` with the requested empty, `None` element, invalid element type, and unsupported top-level type errors. Validation is gated on `hosts` being present in the original play dataset and uses `is_sequence`.
- Updated the existing integration assertion for the revised empty-host error.
- Ran `python -m pytest -q test/units/playbook/test_play.py`: 10 passed.
