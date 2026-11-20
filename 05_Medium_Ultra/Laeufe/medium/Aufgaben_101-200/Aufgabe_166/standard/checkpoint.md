# Checkpoint

Task: restore efficient vaulted variable-file reads through DataLoader.load_from_file caching.
Status: complete.
Changes: added 'none' and 'vaulted' cache modes while preserving boolean behavior; vars_files now uses 'vaulted'; added loader and variable-manager regression tests.
Validation: `python -m pytest -q test/units/parsing/test_dataloader.py test/units/vars/test_variable_manager.py` (44 passed); `git diff --check` passed.
Constraints: used local repository and existing tests only; did not change git history, index baseline, or harness configuration.
