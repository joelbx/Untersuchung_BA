Task: Restore efficient vaulted vars file caching in DataLoader.load_from_file.
Status: Complete.
Changes: Added 'none' and 'vaulted' cache modes while preserving boolean callers; cache writes now respect the mode. VariableManager uses vaulted caching for play vars_files. Added loader and manager regression coverage.
Verification: PYTHONPATH=lib:test/units python -m pytest -q test/units/parsing/test_dataloader.py test/units/vars/test_variable_manager.py (42 passed); git diff --check passed.
