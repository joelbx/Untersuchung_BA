# Checkpoint

- Goal: validate `Play.hosts` with clear parser errors and derive the play name in `get_name` without mutating input data.
- Located implementation in `lib/ansible/playbook/play.py` and existing unit coverage in `test/units/playbook/test_play.py`.
- Implemented dynamic play name derivation and hosts validation with the requested parser errors. Exposed the existing `is_sequence` helper from both collection loader implementations for the specified import path.
- Added unit coverage for valid host forms, input immutability, each validation error, and the YAML mapping regression. Updated the existing integration assertion for the empty-host message.
- Verification: `PYTHONPATH=lib:test pytest -q test/units/playbook` passed (251 tests); checked-out `ansible-playbook --syntax-check` returned parser errors for the empty-host fixture and malformed YAML from stdin; `git diff --check` passed.
