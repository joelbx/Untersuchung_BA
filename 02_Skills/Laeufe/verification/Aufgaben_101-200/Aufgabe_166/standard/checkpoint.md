# Checkpoint

Issue: restore efficient vaulted vars file reads in DataLoader.load_from_file.
Status: implemented 'none' and 'vaulted' cache modes, fixed cache=False writes, and switched play vars_files to vaulted-only caching. Existing boolean callers remain supported.
Verification: PYTHONPATH=lib:test pytest -q test/units/parsing/test_dataloader.py test/units/vars/test_variable_manager.py (44 passed); git diff --check (exit 0).
Regression evidence: before the loader fix, the focused cache tests failed because repeated 'none' and plaintext 'vaulted' loads read only once.
